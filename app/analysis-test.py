from pymongo import MongoClient
# import numpy as np
# import pandas as pd

client = MongoClient('localhost',27017)
db = client.fdatascience # create db name "fdatascience"
print(client.database_names())
print(db.collection_names())

# s_nutrients = db.nutrients.find()
# print(type(s_nutrients))
# nutrients = []
# for i in s_nutrients:
# 	nutrients.append(i)
# print(nutrients)
# print(type(nutrients))
#Food Code

s_con_infants = db.consumption.find( { "Population Class": "Infants" } )
print(type(s_con_infants))
con_infants = []
for i in s_con_infants:
	con_infants.append(i)
# print(con_infants)
# print(type(con_infants))
f_con_infants = []
for i in con_infants:
	dic = {}
	dic["PopClass"] = i["Population Class"]
	dic["FoodName"] = i["Level 1 FoodEx Name"]
	dic["Mean"] = float(i["Mean consumption in grams/ kg body weight per day"])
	dic["Median"] = float(i["Median consumption in grams/ kg body weight per day"])
	f_con_infants.append(dic)
print(f_con_infants)

s_bev_infants = db.beverages_consumption.find( { "Population Class": "Infants" } )
print(type(s_bev_infants))
bev_infants = []
for i in s_bev_infants:
	bev_infants.append(i)
# print(bev_infants)
# print(type(bev_infants))
# Level 1 FoodEx Name
# Mean consumption in grams/ kg body weight per day
# Median consumption in grams/ kg body weight per day
f_bev_infants = []
for i in bev_infants:
	dic = {}
	dic["PopClass"] = i["Population Class"]
	dic["FoodName"] = i["Level 1 FoodEx Name"]
	dic["Mean"] = float(i["Mean consumption in grams/ kg body weight per day"])
	dic["Median"] = float(i["Median consumption in grams/ kg body weight per day"])
	f_bev_infants.append(dic)
print(f_bev_infants)

# mean_weights_inf = []
# median_weights_inf = []
