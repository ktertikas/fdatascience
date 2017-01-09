from pymongo import MongoClient
import numpy as np
from weights import getConDict
import json

# To call function getConDict from weights.py
client = MongoClient('localhost',27017)
db = client.fdatascience # create db name "fdatascience"

s_popclass = db.consumption.distinct("Population Class")
for i in s_popclass:
	# "getConDict" function to clean the data for the second time
	getConDict(json.loads('{"Population Class": "'+ str(i) + '"}'))