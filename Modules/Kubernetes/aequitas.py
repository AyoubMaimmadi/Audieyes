import pandas as pd
from aequitas.group import Group
from aequitas.bias import Bias
from aequitas.plotting import Plot

data = {
    'score': [0, 1, 0, 1, 1, 0, 0, 1, 1, 0],  # Model predictions
    'label_value': [0, 1, 0, 1, 1, 0, 1, 0, 1, 0],  # Actual values
    'caption': ['male', 'female', 'male', 'female', 'male', 'female', 'male', 'female', 'male', 'female']
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Initialize Aequitas Group and Bias objects
group = Group()
bias = Bias()

# Get group metrics
xtab, _ = group.get_crosstabs(df)

# Calculate bias metrics
bdf = bias.get_disparity_predefined_groups(xtab, original_df=df, ref_groups_dict={'image': 'caption'}, alpha=0.05)

# Plot bias metrics
plot = Plot()
plot.plot_disparity(bdf, metrics=['pprev', 'ppr'], attributes=['caption'])

# Save results
bdf.to_csv('bias_audit_results.csv')
