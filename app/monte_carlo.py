import random
from pymongo import MongoClient
import numpy as np
from median_nutrients import getMedianNutr


dic_nutr = getMedianNutr()
print(dic_nutr["vegetables and vegetable products"])

client = MongoClient('localhost',27017)
db = client.fdatascience 
infants = db.consumption_clean.find({"PopClass":"Adults"})
number = infants.count()
k = 0
sample = 1000
sample_arr = np.zeros((sample, number))
names = []
# print(sample_arr)
# print(count)
count = np.zeros(number)
for i in infants:
	for j in range(1, sample):
			x = random.random()
			if x <= i["Percentage"]:
				sample_arr[j-1,k] = i["Median"]	
				count[k] = count[k] + 1
			else:
				sample_arr[j-1,k] = 0.0
	names.append(i["FoodName"])
	k = k + 1
print(sample_arr)
print(count)
print(names)

