from cassandra.cluster import Cluster

cluster = Cluster(['127.0.0.1'])  
session = cluster.connect('ml_features')

def retrieve_features():
    query = "SELECT feature_id, feature_name, feature_values, timestamp FROM features"
    rows = session.execute(query)
    for row in rows:
        print(f"ID: {row.feature_id}, Name: {row.feature_name}, Values: {row.feature_values}, Timestamp: {row.timestamp}")

retrieve_features()

cluster.shutdown()
