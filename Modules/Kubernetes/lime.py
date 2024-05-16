import lime
import lime.lime_tabular
shap = lime
import numpy as np
import pandas as pd
import xgboost

X, y = shap.datasets.coco_karpathy_dataset()
model = xgboost.XGBRegressor().fit(X, y)

# Initialize LIME explainer
explainer = lime.lime_tabular.LimeTabularExplainer(X, feature_names=X.columns, class_names=['caption'], verbose=True, mode='regression')

# Select a data point to explain
i = 25
exp = explainer.explain_instance(X.iloc[i], model.predict, num_features=10)

# Show explanation
exp.show_in_notebook(show_all=False)
