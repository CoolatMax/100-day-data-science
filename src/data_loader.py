from pathlib import Path
import pandas as pd
import requests
from typing import Optional


def download_file(url: str, save_path: str) -> Path:
    """Download a file from a URL to a specified local directory."""
    path = Path(save_path)
    path.parent.mkdir(parents=True, exist_ok=True)

    response = requests.get(url, stream=True)
    response.raise_for_status()

    with open(path, "wb") as f:
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)

    print(f"Downloaded: {path}")
    return path


def load_csv(file_path: str, use_parquet_cache: bool = False) -> pd.DataFrame:
    """
    Load a CSV file safely into a Pandas DataFrame.
    Optionally saves/loads a Parquet version for faster reading on subsequent runs.
    """
    path = Path(file_path)
    parquet_path = path.with_suffix(".parquet")

    if use_parquet_cache and parquet_path.exists():
        print(f"Loading cached Parquet: {parquet_path}")
        return pd.read_parquet(parquet_path)

    if not path.exists():
        raise FileNotFoundError(f"File not found at: {path}")

    df = pd.read_csv(path)
    
    if use_parquet_cache:
        df.to_parquet(parquet_path, index=False)
        print(f"Cached data to: {parquet_path}")

    return df