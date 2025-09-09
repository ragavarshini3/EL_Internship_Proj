from src.data_prep import load_data, clean_data
from src.features import encode_features
from src.train import split_data, train_models
from src.evaluate import evaluate_model
from src.explainability import shap_summary

def main():
    # 1. Load + clean dataset
    print("🔹 Loading and cleaning data...")
    df = load_data("data/processed/hr_data_for_tableau.csv")
    df = clean_data(df)

    # 2. Encode categorical features
    print("🔹 Encoding features...")
    df = encode_features(df)

    # 3. Train/test split + train models
    print("🔹 Splitting data and training models...")
    X_train, X_test, y_train, y_test = split_data(df)
    log_model, tree_model = train_models(X_train, y_train)

    # 4. Evaluate both models
    print("🔹 Evaluating Logistic Regression...")
    evaluate_model(log_model, X_test, y_test, "Logistic Regression")

    print("🔹 Evaluating Decision Tree...")
    evaluate_model(tree_model, X_test, y_test, "Decision Tree")

    # 5. SHAP Explainability
    print("🔹 Running SHAP explainability...")
    shap_summary(tree_model, X_test, "tree")

    print("✅ Pipeline finished! Check shap_summary.png for feature importance.")

if __name__ == "__main__":
    main()