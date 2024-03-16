from cassandra.cluster import Cluster
from great_expectations.data_context import DataContext

def connect_to_cassandra():
    cluster = Cluster(['127.0.0.1'])
    session = cluster.connect('ml_features')
    return session

def validate_data_with_great_expectations(data):
    data_context = DataContext('path_to_your_great_expectations_context')
    batch = data_context.get_batch('batch_request')
    validation_result = data_context.run_validation_operator('action_list_operator', [batch])
    return validation_result['success']

def store_features(session, feature_name, feature_values):
    from uuid import uuid4
    import datetime
    feature_id = uuid4()
    timestamp = datetime.datetime.now()
    query = """
    INSERT INTO features (feature_id, feature_name, feature_values, timestamp)
    VALUES (%s, %s, %s, %s)
    """
    session.execute(query, (feature_id, feature_name, feature_values, timestamp))

def retrieve_features(session):
    query = "SELECT feature_id, feature_name, feature_values, timestamp FROM features"
    rows = session.execute(query)
    for row in rows:
        print(f"ID: {row.feature_id}, Name: {row.feature_name}, Values: {row.feature_values}, Timestamp: {row.timestamp}")

def main():
    raw_data = 'https://storage.googleapis.com/sfr-vision-language-research/datasets/flickr30k_test.json'
    if validate_data_with_great_expectations(raw_data):
        session = connect_to_cassandra()
        processed_data = raw_data  
        store_features(session, "example_feature", processed_data)
        retrieve_features(session)
    else:
        print("Data validation failed.")

if __name__ == "__main__":
    main()
