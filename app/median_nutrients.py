from pymongo import MongoClient
import numpy as np
import json
import math

# Function to calculate the median values for every nutrient in a food group defined by the key parameter
def getMedianNutrByFoodGrp(key):
	client = MongoClient('localhost',27017)
	db = client.fdatascience # create db name "fdatascience"
	nutr_keys = ['VitaminC', 'Fat', 'VitaminK', 'Nitrogen', 'Cholesterol', 'EnergyJ', 'VitaminD', 'Glucose', 'Protein', 'Sugars', 'Carbohydrate', 'VitaminB12', 'VitaminE', 'Lactose', 'Sucrose', 'VitaminB6', 'Water', 'EnergyCal']
	nutrc_foodcode = db.nutrients_clean.distinct("FoodCode")
	dic={}
	for j in nutr_keys:
		nutr_key_value = db.nutrients_clean.find( {j:{'$ne':None}, "FoodCode":key}, {'_id':0, j:1} )
		temp = np.array([])
		for k in nutr_key_value:
			temp = np.append(temp, k[j])
		# dic["FoodCode"] = key
		median = np.median(temp)
		# If the median value is not a number we set it to 0.0
		if (math.isnan(median)):
			dic[j] = 0.0
		else:
			dic[j] = median
	return (dic)

# Function to calculate the median values for every nutrient in each food group
def getMedianNutr():
	client = MongoClient('localhost',27017)
	db = client.fdatascience # create db name "fdatascience"
	nutr_keys = ['VitaminC', 'Fat', 'VitaminK', 'Nitrogen', 'Cholesterol', 'EnergyJ', 'VitaminD', 'Glucose', 'Protein', 'Sugars', 'Carbohydrate', 'VitaminB12', 'VitaminE', 'Lactose', 'Sucrose', 'VitaminB6', 'Water', 'EnergyCal']
	nutrc_foodcode = db.nutrients_clean.distinct("FoodCode")
	dic={}
	for i in nutrc_foodcode:
		dic[i]={}
		for j in nutr_keys:
			nutr_key_value = db.nutrients_clean.find( {j:{'$ne':None}, "FoodCode":i}, {'_id':0, j:1} )
			temp = np.array([])
			for k in nutr_key_value:
				temp = np.append(temp, k[j])
			median = np.median(temp)
			# If the median value is not a number we set it to 0.0
			if (math.isnan(median)):
				dic[i][j] = 0.0
			else:
				dic[i][j] = median
	# print(dic)
	return (dic)
