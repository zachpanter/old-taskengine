from pymongo import MongoClient

def connectToMongoServer():
    # Connect to the default running database server
    client = MongoClient() #client = MongoClient('mongodb://localhost:27017') OR client = MongoClient('localhost',27017)

    # Select a database
    db = client.taskengine #db = client['taskengine']

    # Access a collection
    my_collection = db.phases  #my_collection = db['phases']