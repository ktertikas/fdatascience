from pymongo import MongoClient
import numpy as np
# import pandas as pd

client = MongoClient('localhost',27017)
db = client.fdatascience # create db name "fdatascience"
# nutrients
# consumption
# beverages_consumption
print(client.database_names())
print(db.collection_names())

s_infants = db.consumption.find( { "Population Class": "Infants" } )
print(type(s_infants))
con_infants = []
for i in s_infants:
	con_infants.append(i)
# print(infants)
# print(type(infants))
# Level 1 FoodEx Name
# Mean consumption in grams/ kg body weight per day
# Median consumption in grams/ kg body weight per day

mean_weights_inf = []
median_weights_inf = []

for i in con_infants:
	median_weights_inf.append(float(i["Median consumption in grams/ kg body weight per day"]))
	mean_weights_inf.append(float(i["Mean consumption in grams/ kg body weight per day"]))

x = np.array(mean_weights_inf)
y = np.array(median_weights_inf)
# print(x)
w_mean_inf = np.true_divide(x, x.sum())
w_median_inf = np.true_divide(y, y.sum())
# print(x)