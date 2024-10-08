import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats
import os

# read csv
path = os.path.abspath("lab1/data/data.csv")
data_df = pd.read_csv(path)
sequence = data_df["values"]
data = data_df["values"].values

# 1. Рассчёт математического ожидания, дисперсии, стандартного отклонения, коэффициента вариации

# среднее арифметическое (arithmetic mean)
mean = np.mean(data)
# дисперсия (variance)
# ddof = delta degrees of freedom (скорректированная дисперсия)
# т.е. если степень свободы 1, то мы корректируем выборку как / (n - 1)
variance = np.var(data, ddof=1)
# std = standard deviation (стандартное отклонение)
std_dev = np.std(data, ddof=1)
# коэффициент вариации
# |- показывает относительное отклонение данных от ср. значения в процентах
coef_variation = (std_dev / mean) * 100

# Доверительные интервалы для математического ожидания
# |- (с доверительными вероятностями 0.9, 0.95, 0.99)
confidence_intervals = {}
for confidence in [0.9, 0.95, 0.99]:
    ci = stats.t.interval(
        confidence, len(data) - 1, loc=mean, scale=std_dev / np.sqrt(len(data))
    )
    confidence_intervals[confidence] = ci


# Автокорреляционный анализ
lag_values = range(1, 11)  # Сдвиги от 1 до 10
autocorrelation_coeffs = [sequence.autocorr(lag) for lag in lag_values]

# Вывод значений коэффициентов автокорреляции
print("Коэффициенты автокорреляции со сдвигом от 1 до 10:")
for lag, coeff in zip(lag_values, autocorrelation_coeffs):
    print(f"Сдвиг {lag}: {coeff:.4f}")


# 5. Аппроксимация распределения
# На основе коэффициента вариации можно попробовать различные распределения
if coef_variation < 30:
    distribution = "Равномерное распределение"
    params = stats.uniform.fit(data)
    x = np.linspace(np.min(data), np.max(data), 100)
    y = stats.uniform.pdf(x, *params)
elif coef_variation >= 30 and coef_variation < 100:
    distribution = "Экспоненциальное распределение"
    params = stats.expon.fit(data)
    x = np.linspace(np.min(data), np.max(data), 100)
    y = stats.expon.pdf(x, *params)
else:
    distribution = "Гиперэкспоненциальное распределение"
    # гипотетические параметры для иллюстрации

# 6. Сравнительный анализ между сгенерированной последовательностью и исходной
# Здесь можно сгенерировать последовательность по выбранному распределению
simulated_data = stats.uniform.rvs(*params, size=len(data))  # Генерация данных

# Построение сравнительного графика
autocorrelation2 = [
    np.corrcoef(simulated_data[:-lag], simulated_data[lag:])[0, 1] for lag in lag_values
]

# Вывод значений коэффициентов автокорреляции
print("Коэффициенты автокорреляции ГЧП со сдвигом от 1 до 10:")
for lag, coeff in zip(lag_values, autocorrelation2):
    print(f"Сдвиг {lag}: {coeff:.4f}")

plt.figure(figsize=(10, 6))
plt.stem(range(1, 11), autocorrelation2, basefmt=" ")
plt.title("Автокорреляционный анализ сгенерированной ЧП (сдвиг 1-10)")
plt.xlabel("Сдвиг")
plt.ylabel("Коэффициент автокорреляции")
plt.grid(True)
plt.show()

# Вывод результатов
results = {
    "Математическое ожидание": mean,
    "Дисперсия": variance,
    "Среднеквадратическое отклонение": std_dev,
    "Коэффициент вариации (%)": coef_variation,
    "Доверительные интервалы": confidence_intervals,
}

df_results = pd.DataFrame.from_dict(results, orient="index", columns=["Значение"])
print(df_results)
print(coef_variation)
