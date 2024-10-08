import math
import random
import matplotlib.pyplot as plt

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


# Генерация случайных величин
generated_data = generate_erlang(k, lambda_param)

# Визуализация
plt.figure(figsize=(10, 6))
plt.hist(
    generated_data,
    bins=30,
    density=True,
    alpha=0.7,
    edgecolor="black",
    label="Сгенерированные данные",
)

# Настройки графика
plt.title("Генерация случайных величин по распределению Эрланга")
plt.xlabel("Значение")
plt.ylabel("Плотность вероятности")
plt.legend()
plt.grid(True)
plt.show()
