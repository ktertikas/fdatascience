from pymongo import MongoClient
import numpy as np
from nutrients-clean import getNutr

client = MongoClient('localhost',27017)
db = client.fdatascience # create db name "fdatascience"
print(client.database_names())
print(db.collection_names())

getDict(json.loads('{"Food Code": "grains and grain-based products"}'))

# s_nutrients = db.nutrients.find({ "Food Code": "grains and grain-based products" })
# print(type(s_nutrients))
# nutrients = []
# for i in s_nutrients:
# 	nutrients.append(i)
# print(nutrients)
# print(type(nutrients))
# Food Code

# s_popclass = db.consumption.distinct("Population Class")
# print(s_popclass)
# for i in s_popclass:
# 	# print()
# 	getDict(json.loads('{"Population Class": "'+ str(i) + '"}'))