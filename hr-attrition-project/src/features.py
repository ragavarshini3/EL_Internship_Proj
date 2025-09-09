import pandas as pd
from sklearn.preprocessing import LabelEncoder

def encode_features(df: pd.DataFrame) -> pd.DataFrame:
    """Convert categorical columns to numeric"""
    le = LabelEncoder()
    for col in df.select_dtypes(include=['object']).columns:
        df[col] = le.fit_transform(df[col])
    return df
