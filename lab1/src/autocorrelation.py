import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.graphics.tsaplots import plot_acf
import os

# Чтение данных из CSV-файла
path = os.path.abspath("lab1/data/data.csv")
data = pd.read_csv(path)

# Предположим, что данные лежат в столбце 'value'
sequence = data['values']

# Автокорреляционный анализ
lag_values = range(1, 11)  # Сдвиги от 1 до 10
autocorrelation_coeffs = [sequence.autocorr(lag) for lag in lag_values]

# Вывод значений коэффициентов автокорреляции
print("Коэффициенты автокорреляции со сдвигом от 1 до 10:")
for lag, coeff in zip(lag_values, autocorrelation_coeffs):
    print(f"Сдвиг {lag}: {coeff:.4f}")

# Графическое представление автокорреляции
plt.figure(figsize=(10, 4))
plt.bar(range(1, 11), autocorrelation_coeffs)
plt.title('Автокорреляция сгенерированной ЧП (сдвиг от 1 до 10)')
plt.xlabel('Сдвиг')
plt.ylabel('Коэффициент автокорреляции')
plt.show()

# Вывод обоснования
threshold = 0.2  # Порог для определения случайности
is_random = all(abs(coeff) < threshold for coeff in autocorrelation_coeffs)
if is_random:
    print("\nПоследовательность может считаться случайной.")
else:
    print("\nПоследовательность не является случайной.")
