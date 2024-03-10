from datetime import timedelta
from feast import Entity, FeatureView, ValueType, FileSource

# Define an entity
image_id = Entity(name="image_id", value_type=ValueType.INT64, description="Image ID")

# Define a file source
file_source = FileSource(
    path="data.csv",
    event_timestamp_column="event_timestamp",
)

# Define a feature view
caption_feature_view = FeatureView(
    name="caption_feature_view",
    entities=["image_id"],
    ttl=timedelta(days=1),
    batch_source=file_source,
)

