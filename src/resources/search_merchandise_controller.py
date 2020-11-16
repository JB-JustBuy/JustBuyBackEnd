from flask_restful import Resource, request


class SearchMerchandiseController(Resource):
    def get(self):
        key_word = request.args.get("key_word")

        return {
            "message": "",
            "key_word": key_word
        },  200