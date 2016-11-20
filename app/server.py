import tornado.ioloop
import tornado.web
import tornado.websocket
from pymongo import MongoClient
from bson.objectid import ObjectId
import json, ast


client = MongoClient('localhost',27017)
db = client.fdatascience
# db.app.insert_one({
# 	'name' : 'Top'
# 	})
top = db.app.find()

# print top
for i in top:
	print i["name"]
