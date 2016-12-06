from pymongo import MongoClient
import numpy as np
from nutrients_clean import getNutr
import json

client = MongoClient('localhost',27017)
db = client.fdatascience # create db name "fdatascience"
print(client.database_names())
print(db.collection_names())

nutr_foodcode = db.nutrients.distinct("Food Code")
for i in nutr_foodcode:
	getNutr(json.loads('{"Food Code": "'+ str(i) + '"}'))