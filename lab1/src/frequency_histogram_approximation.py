import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats
import os

# Read the data from CSV file
path = os.path.abspath("lab1/data/data.csv")
data_df = pd.read_csv(path)
sequence = data_df["values"]

# Plotting the histogram of the distribution
plt.figure(figsize=(10, 6))
count, bins, ignored = plt.hist(
    sequence, bins=40, density=True, edgecolor="black", alpha=0.7, label="Гистограмма"
)

# Mean and variance from the sequence
mean = np.mean(sequence)
variance = np.var(sequence, ddof=1)

# Calculating Erlang distribution parameters
k = int((mean**2) / variance)  # Order of the Erlang distribution
scale = mean / k  # Scale parameter for Erlang (1/lambda)

# Generate x values for plotting the Erlang distribution
x = np.linspace(min(sequence), max(sequence), 1000)
erlang_dist = stats.erlang.pdf(x, k, scale=scale)

# Plot the Erlang distribution on the histogram
plt.plot(x, erlang_dist, "r-", lw=2, label=f"Эрланг k={k}")

# Labels and title
plt.title("Гистограмма распределения частот с аппроксимацией Эрланга")
plt.xlabel("Значение")
plt.ylabel("Плотность вероятности")
plt.legend()

# Show the plot
plt.grid(True)
plt.show()
