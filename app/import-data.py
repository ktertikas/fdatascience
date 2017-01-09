from pymongo import MongoClient
import csv
import json

nu_file = open('nutrients.CSV')
con_file = open('consumption.CSV')
bev_file = open('beverages_consumption.CSV')
nu_data = csv.DictReader(nu_file, delimiter=';')
con_data = csv.DictReader(con_file, delimiter=';')

client = MongoClient('localhost',27017)
db = client.fdatascience # create db name "fdatascience"
nu_coll = db.nutrients # create collection name "nutrients"
con_coll = db.consumption # create collection name "consumption"

for i in nu_data:
	nu_coll.insert_one(i)
for i in con_data:
	con_coll.insert_one(i)

print(client.database_names())
print(db.collection_names())