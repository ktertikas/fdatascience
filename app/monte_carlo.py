import random
from pymongo import MongoClient
import numpy as np

client = MongoClient('localhost',27017)
db = client.fdatascience 
infants = db.consumption_clean.find({"PopClass":"Infants"})
number = infants.count()
k = 0
count = np.zeros(number)
print(count)
for i in infants:
	for j in range(1, 1000):
			x = random.random()
			if x <= i["Percentage"]:
				count[k] = count[k] + 1
	k = k + 1
print(count)