import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats
import os

# Чтение данных из CSV файла
# Предположим, что данные хранятся в столбце с именем 'data'
path = os.path.abspath('lab1')
print(f"Path to data: {path}/data/data.csv")
data_df = pd.read_csv(f"{path}/data/data.csv")
data = data_df['data'].values

# 1. Рассчёт математического ожидания, дисперсии, стандартного отклонения, коэффициента вариации
mean = np.mean(data)
variance = np.var(data, ddof=1)
std_dev = np.std(data, ddof=1)
coef_variation = (std_dev / mean) * 100

# Доверительные интервалы для математического ожидания (с доверительными вероятностями 0.9, 0.95, 0.99)
confidence_intervals = {}
for confidence in [0.9, 0.95, 0.99]:
    ci = stats.t.interval(confidence, len(data) - 1, loc=mean, scale=std_dev / np.sqrt(len(data)))
    confidence_intervals[confidence] = ci

# 2. Построение графика числовой последовательности
plt.figure(figsize=(10, 6))
plt.plot(data, marker='o', linestyle='-', color='b')
plt.title("Числовая последовательность")
plt.xlabel("Индекс")
plt.ylabel("Значение")
plt.grid(True)
plt.show()

# 3. Построение гистограммы распределения частот
plt.figure(figsize=(10, 6))
plt.hist(data, bins=20, edgecolor='black', alpha=0.7)
plt.title("Гистограмма распределения частот")
plt.xlabel("Значение")
plt.ylabel("Частота")
plt.grid(True)
plt.show()

# 4. Автокорреляционный анализ
autocorrelation = [np.corrcoef(data[:-lag], data[lag:])[0, 1] for lag in range(1, 21)]
plt.figure(figsize=(10, 6))
plt.stem(range(1, 21), autocorrelation, basefmt=" ")
plt.title("Автокорреляционный анализ (сдвиг 1-20)")
plt.xlabel("Сдвиг")
plt.ylabel("Коэффициент автокорреляции")
plt.grid(True)
plt.show()

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

# Построение гистограммы и плотности аппроксимированного распределения
plt.figure(figsize=(10, 6))
plt.hist(data, bins=20, density=True, edgecolor='black', alpha=0.7, label='Данные')
plt.plot(x, y, 'r-', lw=2, label=f'{distribution}')
plt.title(f"Аппроксимация закона распределения - {distribution}")
plt.xlabel("Значение")
plt.ylabel("Плотность вероятности")
plt.legend()
plt.grid(True)
plt.show()

# 6. Сравнительный анализ между сгенерированной последовательностью и исходной
# Здесь можно сгенерировать последовательность по выбранному распределению
simulated_data = stats.uniform.rvs(*params, size=len(data))  # Генерация данных

# Построение сравнительного графика
plt.figure(figsize=(10, 6))
plt.plot(data, label="Исходная последовательность", marker='o', linestyle='-', color='b')
plt.plot(simulated_data, label="Сгенерированная последовательность", marker='x', linestyle='--', color='r')
plt.title("Сравнение исходной и сгенерированной последовательностей")
plt.xlabel("Индекс")
plt.ylabel("Значение")
plt.legend()
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

df_results = pd.DataFrame.from_dict(results, orient='index', columns=["Значение"])
print(df_results)
