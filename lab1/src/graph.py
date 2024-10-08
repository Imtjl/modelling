import pandas as pd
import matplotlib.pyplot as plt
import os

# Чтение данных из CSV-файла
path = os.path.abspath("lab1/data/data.csv")
data = pd.read_csv(path)

# Печать первых 5 строк для проверки
print(data.head())

# Извлечение значений
sequence = data["values"].tolist()

# Номера индексов для оси X
x_values = list(range(len(sequence)))

# Построение графика
plt.plot(x_values, sequence)
plt.title("График значений последовательности")
plt.xlabel("Индекс")
plt.ylabel("Значение")
plt.grid()
plt.show()
