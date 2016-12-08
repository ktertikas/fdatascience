from pymongo import MongoClient
import numpy as np
from weights import getConDict, getBevDict
import json
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

# s_con_infants = db.consumption.find( { "Population Class": "Infants" } )
# print(type(s_con_infants))
# con_infants = []
# for i in s_con_infants:
# 	con_infants.append(i)
# # print(con_infants)
# # print(type(con_infants))

# mean_weights_inf = []
# median_weights_inf = []
# for i in con_infants:
# 	median_weights_inf.append(float(i["Median consumption in grams/ kg body weight per day"]))
# 	mean_weights_inf.append(float(i["Mean consumption in grams/ kg body weight per day"]))
# x = np.array(mean_weights_inf)
# y = np.array(median_weights_inf)
# w_mean_inf = np.true_divide(x, x.sum())
# w_median_inf = np.true_divide(y, y.sum())
# # print(w_mean_inf)
# # print(w_median_inf)

# f_con_infants = []
# count_row=0
# for i in con_infants:
# 	dic = {}
# 	dic["PopClass"] = i["Population Class"]
# 	dic["FoodName"] = i["Level 1 FoodEx Name"]
# 	dic["Mean"] = float(i["Mean consumption in grams/ kg body weight per day"])
# 	dic["MeanWeight"] = w_mean_inf[count_row]
# 	dic["Median"] = float(i["Median consumption in grams/ kg body weight per day"])
# 	dic["MedianWeight"] = w_median_inf[count_row]
# 	f_con_infants.append(dic)
# 	count_row+=1
# print(f_con_infants)

# s_bev_infants = db.beverages_consumption.find( { "Population Class": "Infants" } )
# print(type(s_bev_infants))
# bev_infants = []
# for i in s_bev_infants:
# 	bev_infants.append(i)
# # print(bev_infants)
# # print(type(bev_infants))

# mean_weights_inf = []
# median_weights_inf = []
# for i in bev_infants:
# 	median_weights_inf.append(float(i["Median consumption in grams/ kg body weight per day"]))
# 	mean_weights_inf.append(float(i["Mean consumption in grams/ kg body weight per day"]))
# x = np.array(mean_weights_inf)
# y = np.array(median_weights_inf)
# w_mean_inf = np.true_divide(x, x.sum())
# w_median_inf = np.true_divide(y, y.sum())

# f_bev_infants = []
# count_row=0
# for i in bev_infants:
# 	dic = {}
# 	dic["PopClass"] = i["Population Class"]
# 	dic["FoodName"] = i["Level 1 FoodEx Name"]
# 	dic["Mean"] = float(i["Mean consumption in grams/ kg body weight per day"])
# 	dic["MeanWeight"] = w_mean_inf[count_row]
# 	dic["Median"] = float(i["Median consumption in grams/ kg body weight per day"])
# 	dic["MedianWeight"] = w_median_inf[count_row]
# 	f_bev_infants.append(dic)
# 	count_row+=1
# print(f_bev_infants)

s_popclass = db.consumption.distinct("Population Class")
# print(s_popclass)
for i in s_popclass:
	# print()
	getConDict(json.loads('{"Population Class": "'+ str(i) + '"}'))
	
# s_popclass = db.beverages_consumption.distinct("Population Class")
# # print(s_popclass)
# for i in s_popclass:	
# 	getBevDict(json.loads('{"Population Class": "'+ str(i) + '"}'))