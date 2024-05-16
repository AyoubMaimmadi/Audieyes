import shap
import numpy as np
import pandas as pd
import xgboost

X, y = shap.datasets.coco_karpathy_dataset()
model = xgboost.XGBRegressor().fit(X, y)

# Initialize SHAP explainer
explainer = shap.Explainer(model)

# Compute SHAP values
shap_values = explainer(X)

# Plot SHAP summary
shap.summary_plot(shap_values, X)

# Plot SHAP dependence
shap.dependence_plot("RM", shap_values, X)

# Plot SHAP for a single prediction
shap.plots.waterfall(shap_values[0])
