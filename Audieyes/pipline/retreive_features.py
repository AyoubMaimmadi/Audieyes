from feast import FeatureStore

store = FeatureStore(repo_path=".")

# Retrieve features for a specific image_id
features = store.get_online_features(
    features=["caption_feature_view:caption"],
    entity_rows=[{"image_id": 1007129816}],
).to_dict()

print(features)
