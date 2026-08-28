import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from typing import Optional, List


def set_style(style: str = "whitegrid", palette: str = "deep"):
    """Set global Matplotlib and Seaborn plotting theme."""
    sns.set_theme(style=style, palette=palette)
    plt.rcParams["figure.figsize"] = (10, 6)
    plt.rcParams["font.size"] = 10


def plot_missing_matrix(df: pd.DataFrame, title: str = "Missing Values Heatmap"):
    """Plot a visual matrix showing where missing values are located in a DataFrame."""
    plt.figure(figsize=(12, 5))
    sns.heatmap(df.isnull(), cbar=False, cmap="viridis", yticklabels=False)
    plt.title(title)
    plt.tight_layout()
    plt.show()


def plot_correlation_heatmap(
    df: pd.DataFrame, cols: Optional[List[str]] = None, annot: bool = True
):
    """Plot a correlation heatmap for numerical columns."""
    data = df[cols] if cols else df.select_dtypes(include=["number"])
    plt.figure(figsize=(10, 8))
    sns.heatmap(data.corr(), annot=annot, fmt=".2f", cmap="coolwarm", vmin=-1, vmax=1)
    plt.title("Feature Correlation Heatmap")
    plt.tight_layout()
    plt.show()