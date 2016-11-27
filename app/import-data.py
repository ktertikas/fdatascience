import os
import json
from pymongo import MongoClient
import numpy as np
import pandas as pd
import csv

# (1)read data from flatfiles (.xlsx / .csv)

# =====test-find directory=====
# cwd = os.getcwd()  # Get the current working directory (cwd)
# files = os.listdir(cwd)  # Get all the files in that directory
# print("Files in '%s': %s" % (cwd, files))

# file = open('test-data.csv')
file = open('first_dataset.CSV')

# =====USE THIS=====
count = 0
f = csv.DictReader(file, delimiter=';')
# print(count)
for i in f:
	print(i)
	
	count+=1
	if(count==2): 
		break

# =====Numpy=====
# data = np.loadtxt(file, delimiter=';', dtype=str)
# data = np.loadtxt(file, delimiter=',', dtype=str, skiprows=1, usecols=0)
# print(type(data))
# print(data)

# key = data[0]
# json_data = {}
# count = 0
# for i in data:
# 	count_row = 0
# 	if(count>0):
# 		for j in i:
# 			json_data[key[count_row]] = j
# 			count_row+=1
# 	count+=1
# 	if(count==2): 
# 		break
# print(key)
# print(json_data)

# =====Pandas=====
# data = pd.read_csv(file, nrows=1)
# print(type(data))
# # print(data.head())
# print(type(data.values))
# print(data.values)

# (2)insert data to db
# client = MongoClient('localhost',27017)
# db = client.fdatascience # create db name "fdatascience"
# collection = db.top # create collection name "top"

# print(client.database_names())
# print(db.collection_names())