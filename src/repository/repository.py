from pymongo import MongoClient


class Repository:
    def __init__(self, data):
        self.client = MongoClient("mongodb://localhost:27017/")
        database = data["database"]
        collection = data['collection']
        cursor = self.client[database]
        self.collection = cursor[collection]
        self.data = data
        # self.client = None
        # self.cursor =  None
        # self.collection = None


    def read(self):
        documents = self.collection.find()
        output = [{item: data[item] for item in data if item != '_id'} for data in documents]
        return output

    def write(self, data):
        new_record = data["document"]
        response = self.collection.insert_one(new_record)
        output = {
            "status": "Successfully Insert.",
            "document_id": str(response.inserted_id)
        }
        return output

    def update(self, data):
        query = data["query"]
        new_value = {"$set": data["new_value"]}
        response = self.collection.update_one(query, new_value)
        output = {
            "status": "Successfully Update ({})".format(response.modified_count)
            if response.modified_count > 0 else "Nothing was updated."
        }
        return output

    def delete(self, data):
        query = data['query']
        response = self.collection.delete_many(query)
        output = {
            "status": 'Successfully Deleted ({})'.format(response.deleted_count)
            if response.deleted_count > 0 else "Document not found."
        }
        return output


if __name__ == '__main__':
    from datetime import datetime
    data = {
        "database": "just_buy",
        "collection": "users"
    }

    mongo_obj = Repository(data)
    output = mongo_obj.read()
    print("Read output:\n", output)

    output = mongo_obj.write({"document": {
        "name": "Jim",
        "age": 19,
        "sex": "man"
    }})
    print("Write output:\n", output)

    data = {
        "query": {
            "name": "Jim"
        },
        "new_value": {
            "name": "Tiff",
            "sex": "woman"
        }
    }
    output = mongo_obj.update(data)
    print("Update output:\n", output)

    data = {
        "query": {
            "sex": "woman"
        }
    }
    output = mongo_obj.delete(data)
    print('"Delete output:\n', output)