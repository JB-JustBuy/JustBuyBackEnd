from src.repository.repository import Repository



class UserRepository(Repository):
    def __init__(self, data):
        super().__init__(data)

    def is_exist(self, data) -> list:
        message = []

        res = self.collection.find({'username': data['username']})
        res = [{item: data[item] for item in data if item != '_id'} for data in res]
        if len(res) != 0:
            message.append('This username has been used')

        res = self.collection.find({'email': data['email']})
        res = [{item: data[item] for item in data if item != '_id'} for data in res]
        if len(res) != 0:
            message.append("This email has registered")
        return message

    def get_users(self) -> list:
        users = self.read()
        return users