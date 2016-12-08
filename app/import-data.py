from pymongo import MongoClient
import csv
import json

nu_file = open('nutrients.CSV')
con_file = open('consumption.CSV')
bev_file = open('beverages_consumption.CSV')
nu_data = csv.DictReader(nu_file, delimiter=';')
con_data = csv.DictReader(con_file, delimiter=';')
# bev_data = csv.DictReader(bev_file, delimiter=';')

# count_break = 0 # test

client = MongoClient('localhost',27017)
db = client.fdatascience # create db name "fdatascience"
nu_coll = db.nutrients # create collection name "nutrients"
con_coll = db.consumption # create collection name "consumption"
# bev_coll = db.beverages_consumption # create collection name "beverages_consumption"

for i in nu_data:
	# print(i)
	nu_coll.insert_one(i)

for i in con_data:
	# print(i)
	con_coll.insert_one(i)

# for i in bev_data:
# 	# print(i)
# 	bev_coll.insert_one(i)

	# count_break+=1 # test
	# if(count_break==2): # test
	# 	break # test

print(client.database_names())
print(db.collection_names())

# ===== Command in Mongo =====
# show databases
# use database
# show collections
# db.collection.find()
# db.collection.count()
# db.collection.drop()
# db.dropDatabase()