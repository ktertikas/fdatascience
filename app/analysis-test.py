from pymongo import MongoClient
# import numpy as np
# import pandas as pd

client = MongoClient('localhost',27017)
db = client.fdatascience # create db name "fdatascience"
# nutrients
# consumption
# beverages_consumption
print(client.database_names())
print(db.collection_names())

sinfants = db.consumption.find( { "Population Class": "Infants" } )
print(type(sinfants))
infants = []
for i in sinfants:
	infants.append(i)
print(infants)
print(type(infants))
# Level 1 FoodEx Name
# Mean consumption in grams/ kg body weight per day
# Median consumption in grams/ kg body weight per day

# mean_weights_inf = []
# median_weights_inf = []

for i in infants:
	float(i["Median consumption in grams/ kg body weight per day"])
	float(i["Mean consumption in grams/ kg body weight per day"])
	i["Level 1 FoodEx Name"]