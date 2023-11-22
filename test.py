import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def descriptive_statistics_plot(data, axes):
    a = data[:, 0]
    b = data[:, 1]
    axes.bar(['Mean', 'Median'], [np.mean(a), np.median(a)], color='blue', alpha=0.7, label='Variable 1')
    axes.bar(['Mean', 'Median'], [np.mean(b), np.median(b)], color='green', alpha=0.7, label='Variable 2')
    axes.legend()
    axes.set_title('Descriptive Statistics: Mean and Median')

def correlation_plot(data, axes):
    sns.heatmap(np.corrcoef(data.T), annot=True, ax=axes)
    axes.set_title('Correlation Analysis')

def histogram_plot(data, axes):
    a = data[:, 0]
    b = data[:, 1]
    axes.hist(a, bins=15, color='blue', alpha=0.7, label='Variable 1')
    axes.hist(b, bins=15, color='green', alpha=0.7, label='Variable 2')
    axes.legend()
    axes.set_title('Histogram of Variables')

def scatter_plot(data, axes):
    a = data[:, 0]
    b = data[:, 1]
    axes.scatter(a, b, alpha=0.7)
    axes.set_xlabel('Variable 1')
    axes.set_ylabel('Variable 2')
    axes.set_title('Scatter Plot of Variable 1 vs Variable 2')

def visualize_data(data):
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))

    descriptive_statistics_plot(data, axes[0, 0])
    correlation_plot(data, axes[0, 1])
    histogram_plot(data, axes[1, 0])
    scatter_plot(data, axes[1, 1])

    plt.tight_layout()
    plt.show()

# 사용 방법:
np.random.seed(0)
data = np.random.randn(100, 2)
visualize_data(data)
