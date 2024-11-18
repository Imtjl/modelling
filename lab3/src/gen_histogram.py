import matplotlib.pyplot as plt
import os


def parse_data_from_file(file_path):
    lower_bounds = []
    upper_bounds = []
    counts = []
    with open(file_path, "r") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue  # Skip empty lines
            parts = line.split()
            try:
                # Handle cases where the lower or upper bound is an underscore
                if parts[0] == "_":
                    lower_bound = None  # Unspecified lower bound
                else:
                    lower_bound = float(parts[0])

                if parts[2] == "_":
                    upper_bound = None  # Unspecified upper bound
                else:
                    upper_bound = float(parts[2])

                count = int(parts[3].replace(",", ""))  # Parse count
                # Assign default values for missing bounds
                if lower_bound is None:
                    lower_bound = upper_bound - 1  # Default width of 1
                if upper_bound is None:
                    upper_bound = lower_bound + 1  # Default width of 1

                lower_bounds.append(lower_bound)
                upper_bounds.append(upper_bound)
                counts.append(count)
            except (ValueError, IndexError):
                continue  # Skip lines with invalid data
    return lower_bounds, upper_bounds, counts


def plot_histogram(lower_bounds, upper_bounds, counts, title, color):
    plt.figure(figsize=(10, 6))

    # Prepare x positions and widths for bars
    x = []
    widths = []
    for lb, ub in zip(lower_bounds, upper_bounds):
        if lb is None:
            lb = ub - 1  # Assume a width of 1 if lower bound is unspecified
        x.append(lb)
        widths.append(ub - lb)

    # Plot the histogram bars
    plt.bar(x, counts, width=widths, align="edge", color=color)

    # Simplify x-axis labels to avoid clutter
    # Show labels at every Nth tick
    N = max(1, len(x) // 10)
    plt.xticks(ticks=x[::N], labels=[f"{xi:.1f}" for xi in x[::N]], fontsize=10)

    plt.title(title, fontsize=16)
    plt.xlabel("Range", fontsize=12)
    plt.ylabel("Frequency", fontsize=12)
    plt.grid(axis="y", alpha=0.75)
    plt.tight_layout()
    plt.show()


histogram_files = [
    ("hist1.txt", "gold", "Histogram for TB_SANUZEL"),
    ("hist2.txt", "mediumslateblue", "Histogram for TB_SHITHOLE1"),
    ("hist3.txt", "coral", "Histogram for TB_SHITHOLE2"),
    ("hist4.txt", "seagreen", "Histogram for TB_BUF"),
]

path = os.path.abspath("data")
for file_path, color, title in histogram_files:
    lower_bounds, upper_bounds, counts = parse_data_from_file(
        os.path.join(path, file_path)
    )
    plot_histogram(lower_bounds, upper_bounds, counts, title, color)
