import pymongo
import logging


class MongoDB:
    def __init__(self):
        self.client = pymongo.MongoClient("mongodb://localhost:27017/")
        self.db = self.client["mydatabase"]
        self.collection = self.db["phones"]
    PHONES_MODEL = ["iphone", "samsung", "xiaomi", "google_pixel"]

    def check_add_valid_path(self, path):
        print("path IS ", path)
        models = path.split("/")
        if models[2] in self.PHONES_MODEL:
            return True, models[2]
        else:
            return False, models[2]

    def insert_data(self, data):
        print("trying to insert ", data)
        self.collection.insert_one(data)
        # print(self.get_all_data())
        return True

    def get_all_data(self):

        cursor = self.collection.find({}, {'_id': 0})
        documents_json_list = list(cursor)
        return documents_json_list
