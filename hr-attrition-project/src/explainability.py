import shap
import matplotlib.pyplot as plt

def shap_summary(model, X_test, model_type="tree"):
    """SHAP global feature importance"""
    if model_type == "tree":
        explainer = shap.TreeExplainer(model)
        shap_values = explainer.shap_values(X_test)
    else:
        explainer = shap.LinearExplainer(model, X_test)
        shap_values = explainer.shap_values(X_test)

    shap.summary_plot(shap_values, X_test)
    plt.savefig("shap_summary.png")
    print("SHAP summary saved as shap_summary.png")

def shap_single(model, X_test, index=0, model_type="tree"):
    """Explain a single prediction"""
    if model_type == "tree":
        explainer = shap.TreeExplainer(model)
        shap_values = explainer.shap_values(X_test)
    else:
        explainer = shap.LinearExplainer(model, X_test)
        shap_values = explainer.shap_values(X_test)

    shap.force_plot(explainer.expected_value[1], shap_values[1][index,:], X_test.iloc[index,:])
