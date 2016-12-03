from pymongo import MongoClient
import numpy as np
import json

client = MongoClient('localhost',27017)
db = client.fdatascience # create db name "fdatascience"
# print(client.database_names())
# print(db.collection_names())

allkeys = db.nutrients_clean.find()
a = []
for i in allkeys:
	if (len(list(i.keys())) == 22) :
		for j in i.keys():
			a.append(j)
		break;
a.remove('_id')
a.remove('Group')
a.remove('FoodCode')
a.remove('FoodName')
print(a)