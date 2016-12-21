from pymongo import MongoClient
import numpy as np
from monte_carlo import montecarlo

client = MongoClient('localhost',27017)
db = client.fdatascience 
population = db.consumption_clean.distinct("PopClass")
kilos = [13.89, 10, 4.6, 1.67 , 1.25, 1.43, 1.43]
nutr_keys = ['VitaminC', 'Fat', 'VitaminK', 'Nitrogen', 'Cholesterol', 'EnergyJ', 'VitaminD', 'Glucose', 'Protein', 'Sugars', 'Carbohydrate', 'VitaminB12', 'VitaminE', 'Lactose', 'Sucrose', 'VitaminB6', 'Water', 'EnergyCal']
visual = db.visualisation # create collection name "visualisation"
k = 0
for i in population:
	print(i)
	print(kilos[k])
	final_arr = montecarlo(i, kilos[k])
	print(final_arr)

	for j in final_arr:
		dictionary = dict(zip(nutr_keys, j))
		dictionary["PopClass"] = i
		# print(dictionary)
		visual.insert_one(dictionary)

	k = k + 1