import os
import json
from pymongo import MongoClient
import numpy as np
import pandas as pd

# (1)read data from flatfiles (.xlsx / .csv)

# =====test-find directory=====
# cwd = os.getcwd()  # Get the current working directory (cwd)
# files = os.listdir(cwd)  # Get all the files in that directory
# print("Files in '%s': %s" % (cwd, files))

file = open('test-data.csv')

# =====Numpy=====
data = np.loadtxt(file, delimiter=',', dtype=str)
# data = np.loadtxt(file, delimiter=',', dtype=str, skiprows=1, usecols=0)
print(type(data))
print(data)

# =====Pandas=====
# data = pd.read_csv(file)
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