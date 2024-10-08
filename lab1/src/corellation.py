import pandas as pd
import numpy as np
import os

# Чтение данных
path_generated = os.path.abspath("lab1/data/random_data.csv")
path_original = os.path.abspath("lab1/data/data.csv")

# Загрузка данных
data_generated = pd.read_csv(path_generated)
data_original = pd.read_csv(path_original)

# Корреляционный анализ между сгенерированной и исходной последовательностями
correlation_coefficient = np.corrcoef(
    data_original["values"], data_generated["values"]
)[0, 1]

print(correlation_coefficient)
