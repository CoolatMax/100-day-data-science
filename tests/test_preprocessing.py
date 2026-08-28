import numpy as np
import pandas as pd
import pytest
from sklearn.preprocessing import MinMaxScaler, StandardScaler

from src.preprocessing import (
    clean_column_names,
    handle_missing_values,
    scale_features,
)


@pytest.fixture
def sample_df():
    """Fixture providing a raw, messy DataFrame for unit testing."""
    return pd.DataFrame(
        {
            " First Name ": ["Alice", "Bob", "Charlie", None],
            "AGE (years)!": [25, np.nan, 35, 40],
            "Salary ($)": [50000, 60000, np.nan, 80000],
        }
    )


def test_clean_column_names(sample_df):
    """Test string standardization: lowercase, snake_case, and special character removal."""
    cleaned_df = clean_column_names(sample_df)

    expected_columns = ["first_name", "age_years", "salary"]
    assert list(cleaned_df.columns) == expected_columns


def test_handle_missing_values_drop(sample_df):
    """Test dropping rows with missing values."""
    df_clean = clean_column_names(sample_df)
    result = handle_missing_values(df_clean, strategy="drop")

    # Original has 4 rows; only rows with zero NaNs should remain (1 row: Charlie)
    assert len(result) == 1
    assert result.isnull().sum().sum() == 0


def test_handle_missing_values_impute_mean(sample_df):
    """Test mean imputation on numerical columns."""
    df_clean = clean_column_names(sample_df)
    result = handle_missing_values(df_clean, strategy="mean", cols=["age_years"])

    # Mean of [25, 35, 40] is 33.333...
    assert result["age_years"].isnull().sum() == 0
    assert np.isclose(result["age_years"].iloc[1], 33.333333)


def test_scale_features_standard(sample_df):
    """Test Z-score scaling (StandardScaler)."""
    df_clean = clean_column_names(sample_df)
    df_imputed = handle_missing_values(df_clean, strategy="mean")

    scaled_df, scaler = scale_features(
        df_imputed, numerical_cols=["age_years", "salary"], method="standard"
    )

    assert isinstance(scaler, StandardScaler)
    assert np.isclose(scaled_df["age_years"].mean(), 0, atol=1e-7)
    assert np.isclose(scaled_df["age_years"].std(ddof=0), 1.0, atol=1e-7)


def test_scale_features_minmax(sample_df):
    """Test range scaling (MinMaxScaler)."""
    df_clean = clean_column_names(sample_df)
    df_imputed = handle_missing_values(df_clean, strategy="mean")

    scaled_df, scaler = scale_features(
        df_imputed, numerical_cols=["age_years", "salary"], method="minmax"
    )

    assert isinstance(scaler, MinMaxScaler)
    assert scaled_df["age_years"].min() == 0.0
    assert scaled_df["age_years"].max() == 1.0