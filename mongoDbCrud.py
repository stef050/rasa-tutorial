from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client['rasa']
applications = db['applications']

class MongoCrud:
    def insert():
        application = {
            "name": "D. targ",
            "email": "m-o-dragons@got.com",
            "appType": "loan"
        }

        applications.insert_one(application)
        return
