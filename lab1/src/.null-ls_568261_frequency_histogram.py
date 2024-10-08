import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

# Read the data from CSV file
path = os.path.abspath("lab1/data/data.csv")

data_df = pd.read_csv(path)
sequence = data_df["values"]

# Plotting the histogram of the distribution
plt.figure(figsize=(10, 6))
plt.hist(sequence, bins=20, edgecolor="black", alpha=0.7)
plt.title("Гистограмма распределения частот для числовой последовательности")
plt.xlabel("Значение")
plt.ylabel("Частота")
plt.grid(True)

# Display the histogram
plt.show()
