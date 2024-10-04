import numpy as np
import matplotlib.pyplot as plt

# Генерация 300 случайных величин по экспоненциальному закону
data = np.random.exponential(scale=1, size=300)

# Визуализация временного ряда
plt.figure(figsize=(10, 4))
plt.plot(data)
plt.title('Экспоненциальный временной ряд')
plt.show()

# Расчет автокорреляций с лагами от 1 до 10
lag_values = range(1, 11)  # Сдвиги от 1 до 10
autocorr = [np.corrcoef(data[:-lag], data[lag:])[0, 1] for lag in lag_values]

# Вывод значений коэффициентов автокорреляции
print("Коэффициенты автокорреляции со сдвигом от 1 до 10:")
for lag, coeff in zip(lag_values, autocorr):
    print(f"Сдвиг {lag}: {coeff:.4f}")

# Визуализация автокорреляций
plt.figure(figsize=(10, 4))
plt.bar(range(1, 11), autocorr)
plt.title('Автокорреляция сгенерированной ЧП (сдвиг от 1 до 10)')
plt.xlabel('Сдвиг')
plt.ylabel('Коэффициент автокорреляции')
plt.show()
