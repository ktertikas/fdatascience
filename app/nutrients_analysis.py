from pymongo import MongoClient
import numpy as np
import json

import matplotlib.pyplot as plt

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

nutrc_foodcode = db.nutrients_clean.distinct("FoodCode")
final=[]
for i in nutrc_foodcode:
	file = open("nutrients_text_output/"+i+".txt", "wb")
	dic={}
	for j in nutr_keys:
		nutr_key_value = db.nutrients_clean.find( {j:{'$ne':None}, "FoodCode":i}, {'_id':0, j:1} )
		temp = np.array([])
		for k in nutr_key_value:
			temp = np.append(temp, k[j])

		# print("Food Code in processing: "+i+" & Key->"+j)
		# plt.hist(temp, bins=20)
		# plt.savefig('nutrients_graphical_output/'+i+'_'+j+'.png')
		# plt.clf()
		# plt.boxplot(temp)
		# plt.savefig('nutrients_graphical_output/boxplot_'+i+'_'+j+'.png')
		# plt.clf()
		# mean_print = "mean value of "+j+" is ;"+str(np.mean(temp))
		# median_print = "median value of "+j+" is ;"+str(np.median(temp))
		# sd_print = "standard deviation value of "+j+" is ;"+str(np.std(temp))
		# file.write(mean_print.encode('utf-8'))
		# file.write(b"\n")
		# file.write(median_print.encode('utf-8'))
		# file.write(b"\n")
		# file.write(sd_print.encode('utf-8'))
		# file.write(b"\n")
		if j == "EnergyCal":
			dic["FoodCode"] = i
			dic[j] = np.median(temp)
	final.append(dic)
	file.close()
# print(final)
# find clean consumption for infants and take median weights for every food group
consum = db.consumption_clean.find({"PopClass":"Infants"})
for i in consum:
	sum1 = 0
	for j in final:
		if i["FoodName"] == j["FoodCode"]:
			print(i["MedianWeight"])
			print(j["EnergyCal"])
			sum1 = sum1 + i["MedianWeight"]*j["EnergyCal"]
print(sum1)
			