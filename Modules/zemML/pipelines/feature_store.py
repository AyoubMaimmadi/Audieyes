from cassandra.cluster import Cluster

def connect_to_cassandra():
    cluster = Cluster(['127.0.0.1'])
    session = cluster.connect('ml_features')
    return session

def process_features(data):
    processed_data = data  
    return processed_data

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

session = connect_to_cassandra()
raw_data = [1.0, 2.0, 3.0] 
processed_data = process_features(raw_data)
store_features(session, "example_feature1", processed_data)
store_features(session, "example_feature2", processed_data)
store_features(session, "example_feature3", processed_data)
store_features(session, "example_feature4", processed_data)
