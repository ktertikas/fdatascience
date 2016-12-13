import random
from pymongo import MongoClient
import numpy as np
from median_nutrients import getMedianNutr


def montecarlo(popClass, kg1):
# print(dic_nutr["vegetables and vegetable products"])
	dic_nutr = getMedianNutr()
	client = MongoClient('localhost',27017)
	db = client.fdatascience 
	infants = db.consumption_clean.find({"PopClass": popClass})
	number = infants.count()
	k = 0
	sample = 5000
	sample_arr = np.zeros((sample, number))
	names = []
	nutr_keys = ['VitaminC', 'Fat', 'VitaminK', 'Nitrogen', 'Cholesterol', 'EnergyJ', 'VitaminD', 'Glucose', 'Protein', 'Sugars', 'Carbohydrate', 'VitaminB12', 'VitaminE', 'Lactose', 'Sucrose', 'VitaminB6', 'Water', 'EnergyCal']
	# print(sample_arr)
	# print(count)
	count = np.zeros(number)
	for i in infants:
		for j in range(0, sample):
				x = random.random()
				if x <= i["Percentage"]:
					sample_arr[j,k] = i["Median"]	
					count[k] = count[k] + 1
				else:
					sample_arr[j,k] = 0.0
		names.append(i["FoodName"])
		k = k + 1
	# print(sample_arr)
	# print(names)

	final_arr = np.zeros((sample,len(nutr_keys)))
	count_sam = 0
	for i in sample_arr:
		# print(i)
		count_fg = 0
		for j in i:
			# print(i[j])
			i_nutr = 0
			for l in nutr_keys:
				final_arr[count_sam][i_nutr] = final_arr[count_sam][i_nutr] + j*dic_nutr[names[count_fg]][l]
				i_nutr = i_nutr + 1
			count_fg = count_fg + 1
		count_sam = count_sam + 1
	# print(final_arr)
	final_arr = np.true_divide(final_arr, kg1)

	# print(final_arr)
	return final_arr
# print(final_arr[:,5])
# print(dic_nutr)
	# for j in range(1, sample):
	# 		if x <= i["Percentage"]:
	# 			sample_arr[j-1,k] = i["Median"]	
	# 			count[k] = count[k] + 1
	# 		else:
	# 			sample_arr[j-1,k] = 0.0
	# names.append(i["FoodName"])
	# k = k + 1
# print(sample_arr)
# print(count)
# print(names)

