﻿import tornado.ioloop
import tornado.web
import tornado.websocket
import json
from pymongo import MongoClient
# from bson.objectid import ObjectId

client = MongoClient('localhost',27017)
db = client.fdatascience # create db name "fdatascience"
collection = db.visualisation # create collection name "app"

# collection.insert_one({ # insert data
# 	'name' : 'Top'
# 	})

print(collection.find())

# top = db.app.find_one()

top = collection.find()
for i in top:
	print(i['name'])
