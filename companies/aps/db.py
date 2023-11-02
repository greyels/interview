from json import dumps

from pymongo import MongoClient


class EarthquakeDataHandler:
    def __init__(self, database_name="aps", collection_name="earthqauke", connection_url='mongodb://localhost:27017/'):
        self.client = MongoClient(connection_url)
        self.database = self.client[database_name]
        self.collection = self.database[collection_name]

    def close_connection(self):
        self.client.close()


class EarthquakeDataInserter(EarthquakeDataHandler):
    def insert_features(self, data):
        # TODO: align incoming data format with the target MongoDB Data Model (README.md)
        self.collection.insert_many(data["features"])
        self.client.close()


class EarthquakeDataRetriever(EarthquakeDataHandler):
    def retrive_by_date(self, start_date, end_date):
        query = {
            "properties.timestamp": {
                "$gte": start_date,
                "$lte": end_date
            }
        }
        cursor = self.collection.find(query)
        feature_collection = {
            "type": "FeatureCollection",
            "features": []
        }
        for document in cursor:
            feature = {
                "type": "Feature",
                "geometry": document.get("geometry"),
                "properties": document.get("properties")
            }
            feature_collection["features"].append(feature)
        return dumps(feature_collection)

    def retrive_by_magnitude(self, min_magnitude, max_magnitude):
        query = {
            "properties.magnitude": {
                "$gte": min_magnitude,
                "$lte": max_magnitude
            }
        }
        cursor = self.collection.find(query)
        feature_collection = {
            "type": "FeatureCollection",
            "features": []
        }
        for document in cursor:
            feature = {
                "type": "Feature",
                "geometry": document.get("geometry"),
                "properties": document.get("properties")
            }
            feature_collection["features"].append(feature)
        return dumps(feature_collection)

    def retrive_by_country(self, country):
        pass

    def retrive_by_bounding_box(self, min_longitude, min_latitude, max_longitude, maximum_latitude):
        pass
