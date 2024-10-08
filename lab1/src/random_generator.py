import math
import random
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os

# Параметры распределения Эрланга
k = 2  # Порядок распределения
lambda_param = 0.0144  # Параметр λ, обратный среднему


# Генерация случайной величины, распределённой по экспоненциальному закону
def generate_exponential(lambda_param):
    return -math.log(random.random()) / lambda_param


# Генератор случайных величин по закону Эрланга
def generate_erlang(k, lambda_param, size=1000):
    erlang_samples = []
    for _ in range(size):
        sample = sum(generate_exponential(lambda_param) for _ in range(k))
        erlang_samples.append(sample)
    return erlang_samples


# Аппроксимация плотности распределения Эрланга
def erlang_pdf(x, k, lambda_param):
    return (lambda_param ** k * x ** (k - 1) * np.exp(-lambda_param * x)) / math.factorial(k - 1)


# Генерация случайных величин
path = os.path.abspath("lab1/data")
generated_data = {
    "values": generate_erlang(k, lambda_param),
}

df = pd.DataFrame(generated_data)
df.to_csv(f"{path}/random_data.csv", index=False)

# Визуализация сгенерированных данных
plt.figure(figsize=(10, 6))
plt.hist(
    generated_data["values"],
    bins=30,
    density=True,
    alpha=0.7,
    edgecolor="black",
    label="Сгенерированные данные",
)

# Создание линии аппроксимации
x_values = np.linspace(0, max(generated_data["values"]), 1000)
pdf_fitted = erlang_pdf(x_values, k, lambda_param)

# Добавление линии аппроксимации на график
plt.plot(x_values, pdf_fitted, 'r-', lw=2, label="Аппроксимация Эрланга (k=2)")

# Настройки графика
plt.title("Генерация случайных величин по распределению Эрланга с аппроксимацией")
plt.xlabel("Значение")
plt.ylabel("Плотность вероятности")
plt.legend()
plt.grid(True)
plt.show()
