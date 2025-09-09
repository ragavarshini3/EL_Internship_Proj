from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import pandas as pd

def evaluate_model(model, X_test, y_test, name="Model"):
    """Evaluate model performance"""
    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    cm = confusion_matrix(y_test, y_pred)
    report = classification_report(y_test, y_pred)

    print(f"\n{name} Accuracy: {acc:.2f}")
    print("Confusion Matrix:\n", cm)
    print("Classification Report:\n", report)

    return {"Model": name, "Accuracy": acc}
