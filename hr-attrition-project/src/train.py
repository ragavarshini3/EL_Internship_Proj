import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier

def split_data(df: pd.DataFrame, target: str = "Attrition"):
    """Split data into train/test"""
    X = df.drop(target, axis=1)
    y = df[target]
    return train_test_split(X, y, test_size=0.2, random_state=42)

def train_models(X_train, y_train):
    """Train Logistic Regression & Decision Tree"""
    log_model = LogisticRegression(max_iter=1000)
    tree_model = DecisionTreeClassifier(max_depth=5, random_state=42)

    log_model.fit(X_train, y_train)
    tree_model.fit(X_train, y_train)

    return log_model, tree_model