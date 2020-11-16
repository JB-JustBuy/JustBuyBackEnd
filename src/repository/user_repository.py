from pymongo import MongoClient

class UserRepository:
    def __init__(self, data):
        self.client = MongoClient("mongodb://localhost:27017/")
        database = data["database"]
        collection = data['collection']
        cursor = self.client[database]
        self.collection = cursor[collection]
        self.data = data

    def read(self):
        documents = self.collection.find()
        output = [{item: data[item] for item in data if item != '_id'} for data in documents]
        return output



if __name__ == '__main__':
    data = {
        "database": "just_buy",
        "collection": "users"
    }

    mongo_obj = UserRepository(data)
    output = mongo_obj.read()
    print("output:\n", output)