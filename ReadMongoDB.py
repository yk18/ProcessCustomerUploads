__author__ = 'ykogan'


import pymongo

def read_mongodb_server_models():
    client = pymongo.MongoClient("localhost", 27017)
    db = client['reference-database']
    posts = db.posts

    result = []
    # these are the server model names existing in the reference-database
    for doc in db["server"].find({}, {'_id':0,'server_model_name':1, 'cpu_model':1}):
        result = result + [doc['server_model_name']]

    return result