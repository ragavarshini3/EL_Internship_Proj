import pandas as pd

def load_data(path: str) -> pd.DataFrame:
    """Load HR dataset"""
    df = pd.read_csv(path)
    return df

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Drop irrelevant cols, handle missing values"""
    drop_cols = ["EmployeeCount", "Over18", "StandardHours"]
    df = df.drop(columns=[c for c in drop_cols if c in df.columns], errors="ignore")
    df = df.dropna()
    return df