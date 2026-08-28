import pandas as pd
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from typing import List, Optional, Tuple, Union


def clean_column_names(df: pd.DataFrame) -> pd.DataFrame:
    """Convert column names to lowercase snake_case."""
    df_clean = df.copy()
    df_clean.columns = (
        df_clean.columns.str.strip()
        .str.lower()
        .str.replace(" ", "_", regex=False)
        .str.replace(r"[^\w\s]", "", regex=True)
    )
    return df_clean


def handle_missing_values(
    df: pd.DataFrame, strategy: str = "drop", cols: Optional[List[str]] = None
) -> pd.DataFrame:
    """
    Handle missing values in a DataFrame.
    Strategies: 'drop', 'mean', 'median', 'mode'
    """
    df_out = df.copy()
    target_cols = cols if cols is not None else df_out.columns

    if strategy == "drop":
        return df_out.dropna(subset=target_cols)

    for col in target_cols:
        if df_out[col].isnull().sum() > 0:
            if strategy == "mean" and pd.api.types.is_numeric_dtype(df_out[col]):
                df_out[col] = df_out[col].fillna(df_out[col].mean())
            elif strategy == "median" and pd.api.types.is_numeric_dtype(df_out[col]):
                df_out[col] = df_out[col].fillna(df_out[col].median())
            elif strategy == "mode":
                df_out[col] = df_out[col].fillna(df_out[col].mode()[0])

    return df_out


def scale_features(
    df: pd.DataFrame, numerical_cols: List[str], method: str = "standard"
) -> Tuple[pd.DataFrame, Union[StandardScaler, MinMaxScaler]]:
    """Scale specified numerical features using StandardScaler or MinMaxScaler."""
    df_scaled = df.copy()
    scaler = StandardScaler() if method == "standard" else MinMaxScaler()

    df_scaled[numerical_cols] = scaler.fit_transform(df_scaled[numerical_cols])
    return df_scaled, scaler