import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt

# Sample data: variance and mean values from user data for 300 values
mean_values = [147.476, 148.874, 162.476, 181.411, 178.538, 175.513]
variances = [2424.613, 4790.369, 9753.9, 14354.424, 15422.509, 15088.212]
sample_sizes = [10, 20, 50, 100, 200, 300]

# Calculating lambda and fitting to Erlang distribution based on the mean values
lambda_values = [1 / mean for mean in mean_values]

# Generate x values for plotting the Erlang distribution
x = np.linspace(0, max(mean_values) * 2, 1000)

# Plot the Erlang distributions for each sample size
plt.figure(figsize=(10, 6))

for i, (mean, var, sample_size) in enumerate(zip(mean_values, variances, sample_sizes)):
    k = int((mean**2) / var)  # Order of the Erlang distribution
    scale = mean / k  # Scale parameter for Erlang (1/lambda)
    erlang_dist = stats.erlang.pdf(x, k, scale=scale)

    # Plot each Erlang distribution
    plt.plot(x, erlang_dist, label=f"Erlang (Sample Size {sample_size}, k={k})")

plt.title("Approximation of Erlang Distributions for Different Sample Sizes")
plt.xlabel("x")
plt.ylabel("Probability Density")
plt.legend()
plt.grid(True)

# Show the plot with Erlang approximations
plt.show()
