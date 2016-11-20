import tornado.ioloop
import tornado.web
import tornado.websocket
from pymongo import MongoClient
from bson.objectid import ObjectId
import json, ast


client = MongoClient('localhost',27017)
db = client.fdatascience
db.app.insert_one({
	'name' : 'Top'
	})
top = db.app.find_one()

collection = db.app # create collection name "app"

print(client.database_names())
print(db.collection_names())