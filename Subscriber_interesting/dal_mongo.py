from pymongo import MongoClient


class DAL_Mongo:

    def __init__(self, host, database, collection, user= None, password= None):
        self.host = host
        self.database = database
        self.collection = collection
        self.user = user
        self.password = password
        self.URI = self.get_URI()
        self.client = None
        self.connect = False


    def get_URI(self):
        if self.user and self.password:
            URI = f"mongodb://{self.user}:{self.password}@{self.host}::27017"
        else:
            URI = f"mongodb://{self.host}:27017"

        return URI


    def open_connection(self):
        """ create connection to mongo db """
        try:
            self.client = MongoClient(self.URI)
            self.client.admin.command("ping")
            self.connect = True
            return True
        except Exception as e:
            self.client = None
            print("Error: ", e)
            return False


    def get_all(self):
        if self.connect:
            db = self.client[self.database]
            collection = db[self.collection]
            data = collection.find()
            return list(data)


    def insert_data(self, massage):
        if self.connect:
            collection = self.database[self.collection]
            try:
                results = collection.insert_one(massage)
                return {"data added successfully: " : massage}
            except Exception as e:
                return {"error : ": e}


    def close_connection(self):
        if self.connect:
            self.client.close()