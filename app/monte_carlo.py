import random
from pymongo import MongoClient
import numpy as np
from median_nutrients import getMedianNutr

# Function to create randomness and a population of 5000 samples 
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

	# We create a random number from 0 to 1.
	# If the percentage of consumption is smaller than this number, we don't count the median consumption for this specific person
	# Otherwise, we count it normally.
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
	
	# We calculate the values of median consumption for every different nutrient for each of the 5000 sample population person
	# and we create a final array that has all these values, each line representing a different person
	# Every column contains the respective nutrient as in the above array nutr_keys
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

