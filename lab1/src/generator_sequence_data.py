import numpy as np
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats
import os

# Генерация 300 случайных величин по экспоненциальному закону
# data = np.random.exponential(scale=1, size=300)
path = os.path.abspath("lab1/data/data.csv")
data_df = pd.read_csv(path)
sequence = data_df["values"]
data = data_df["values"].values
sizes = [10, 20, 50, 100, 200, 300]

# Визуализация временного ряда
plt.figure(figsize=(10, 4))
plt.plot(data)
plt.title("Экспоненциальный временной ряд")
plt.show()

# Коэффициент вариации для полной выборки (N=300)
full_sample_size = 300
full_sample = data[:full_sample_size]
mean_full = np.mean(full_sample)
std_dev_full = np.std(full_sample, ddof=1)
coef_variation_full = (std_dev_full / mean_full) * 100
variance_full = np.var(full_sample, ddof=1)

# Доверительные интервалы для полной выборки
full_confidence_intervals = {}
full_ci_deltas = {}
for confidence in [0.9, 0.95, 0.99]:
    ci_full = stats.t.interval(
        confidence,
        len(full_sample) - 1,
        loc=mean_full,
        scale=std_dev_full / np.sqrt(len(full_sample)),
    )
    full_ci_deltas[confidence] = (ci_full[1] - ci_full[0]) / 2

# Рассчет для подвыборок и относительных отклонений
for i in sizes:
    print(f"\nДля подвыборки из {i} значений:")
    data_sample = data[:i]
    mean = np.mean(data_sample)
    std_dev = np.std(data_sample, ddof=1)
    coef_variation = (std_dev / mean) * 100
    variance = np.var(data_sample, ddof=1)

    # Относительные отклонения
    mean_deviation = (mean - mean_full) / mean_full * 100
    variance_deviation = (variance - variance_full) / variance_full * 100
    std_dev_deviation = (std_dev - std_dev_full) / std_dev_full * 100
    coef_variation_deviation = (
        (coef_variation - coef_variation_full) / coef_variation_full * 100
    )

    # Доверительные интервалы
    confidence_intervals = {}
    ci_deltas = {}
    ci_deviation = {}
    for confidence in [0.9, 0.95, 0.99]:
        ci = stats.t.interval(
            confidence,
            len(data_sample) - 1,
            loc=mean,
            scale=std_dev / np.sqrt(len(data_sample)),
        )
        delta = (ci[1] - ci[0]) / 2
        ci_deltas[confidence] = delta

        # Относительное отклонение дельты доверительного интервала
        ci_deviation[confidence] = (
            (delta - full_ci_deltas[confidence]) / full_ci_deltas[confidence] * 100
        )

        confidence_intervals[confidence] = (
            f"{mean:.3f} ± {delta:.3f} ({ci_deviation[confidence]:.3f}%)"
        )

    # Вывод результатов с отклонениями
    results = {
        "Математическое ожидание": f"{mean:.3f} ({mean_deviation:.3f}%)",
        "Дисперсия": f"{variance:.3f} ({variance_deviation:.3f}%)",
        "Среднеквадратическое отклонение": f"{std_dev:.3f} ({std_dev_deviation:.3f}%)",
        "Коэффициент вариации (%)": f"{coef_variation:.3f} ({coef_variation_deviation:.3f}%)",
        "Доверительный интервал (0.9)": confidence_intervals[0.9],
        "Доверительный интервал (0.95)": confidence_intervals[0.95],
        "Доверительный интервал (0.99)": confidence_intervals[0.99],
    }

    df_results = pd.DataFrame.from_dict(results, orient="index", columns=["Значение"])
    print(df_results)
