from pymongo import MongoClient
import numpy as np
import json

import matplotlib.pyplot as plt
from weights import getConDict, getBevDict

client = MongoClient('localhost',27017)
db = client.fdatascience # create db name "fdatascience"
# print(client.database_names())
# print(db.collection_names())

# allkeys = db.nutrients_clean.find()
# a = []
# for i in allkeys:
# 	if (len(list(i.keys())) == 22) :
# 		for j in i.keys():
# 			a.append(j)
# 		break;
# a.remove('_id')
# a.remove('Group')
# a.remove('FoodCode')
# a.remove('FoodName')
# print(a)
nutr_keys = ['VitaminC', 'Fat', 'VitaminK', 'Nitrogen', 'Cholesterol', 'EnergyJ', 'VitaminD', 'Glucose', 'Protein', 'Sugars', 'Carbohydrate', 'VitaminB12', 'VitaminE', 'Lactose', 'Sucrose', 'VitaminB6', 'Water', 'EnergyCal']

# nutr_key_value = db.nutrients_clean.find( {'VitaminC':{'$ne':None}}, {'_id':0, 'VitaminC':1} )
# temp = np.array([])
# for j in nutr_key_value:
# 	temp = np.append(temp, j['VitaminC'])
# print(temp)

final = np.array([])
for i in nutr_keys:
	nutr_key_value = db.nutrients_clean.find( {i:{'$ne':None}}, {'_id':0, i:1} )
	temp = np.array([])
	for j in nutr_key_value:
		temp = np.append(temp, j[i])
	# plt.hist(temp, bins=20)
	# plt.savefig('hist_'+i+'.png')
	# plt.clf()
	# plt.boxplot(temp)
	# plt.savefig('boxplot_'+i+'.png')
	# plt.clf()
	print("mean value of "+i+" is "+str(np.mean(temp)))
	print("median value of "+i+" is "+str(np.median(temp)))
	print("standard deviation value of "+i+" is "+str(np.std(temp)))