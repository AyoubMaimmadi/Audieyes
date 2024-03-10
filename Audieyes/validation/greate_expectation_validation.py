import great_expectations as ge
import pandas as pd

data = [{
        "image": "flickr30k-images/1007129816.jpg",
        "caption": [
            "The man with pierced ears is wearing glasses and an orange hat.",
            "A man with glasses is wearing a beer can crocheted hat.",
            "A man with gauges and glasses is wearing a Blitz hat.",
            "A man in an orange hat starring at something.",
            "A man wears an orange hat and glasses."
        ]
        },
        {
        "image": "flickr30k-images/1009434119.jpg",
        "caption": [
            "A black and white dog is running in a grassy garden surrounded by a white fence.",
            "A Boston Terrier is running on lush green grass in front of a white fence.",
            "A black and white dog is running through the grass.",
            "A dog runs on the green grass near a wooden fence.",
            "A Boston terrier is running in the grass."
        ]
        },
        {
        "image": "flickr30k-images/101362133.jpg",
        "caption": [
            "A young female student performing a downward kick to break a board held by her Karate instructor.",
            "Girl about to kick a piece of wood in half while karate instructor holds it",
            "A girl kicking a stick that a man is holding in tae kwon do class.",
            "A girl in karate uniform breaking a stick with a front kick.",
            "A girl breaking boards by using karate."
        ]
    }],

df = pd.DataFrame(data)

# Convert the DataFrame to a Great Expectations dataset
dataset = ge.from_pandas(df)

# Existing expectations
dataset.expect_column_to_exist("image")
dataset.expect_column_values_to_be_of_type("image", "string")

# Existing expectations
dataset.expect_column_to_exist("caption")
dataset.expect_column_values_to_be_of_type("caption", "string")

# Additional expectations
# Check for non-empty columns
dataset.expect_column_values_to_not_be_null("image")
dataset.expect_column_values_to_not_be_null("caption")

# Check for unique images
dataset.expect_column_values_to_be_unique("image")
dataset.expect_column_values_to_be_unique("caption")

# Check that each caption list has at least one caption and doesn't exceed a maximum (e.g., 5 captions)
dataset.expect_column_values_to_be_between("caption", min_value=1, max_value=5, strict_min=True, strict_max=True)

# Custom expectation for non-empty captions within the list
def expect_list_of_strings_to_not_be_empty(column_values):
    all_non_empty = all(all(caption.strip() for caption in captions) for captions in column_values)
    return {
        "success": all_non_empty
    }

# Run validation for the defined expectations
results = dataset.validate()
print(results)
