from pymongo import MongoClient
import numpy as np
from nutrients_clean import getNutr
import json

# To call function getNutr from nutrients_clean.py
client = MongoClient('localhost',27017)
db = client.fdatascience # create db name "fdatascience"

nutr_foodcode = db.nutrients.distinct("Food Code")
for i in nutr_foodcode:
	# "getNutr" function to clean the data from the collection "nutrients" for the second time
	getNutr(json.loads('{"Food Code": "'+ str(i) + '"}'))