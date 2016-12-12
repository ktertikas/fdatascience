from pymongo import MongoClient
import numpy as np
from monte_carlo import montecarlo

client = MongoClient('localhost',27017)
db = client.fdatascience 
population = db.consumption_clean.distinct("PopClass")
kilos = [20, 10, 4.6, 1.67 , 1.25, 1.43, 1.43]
k = 0
for i in population:
	print(i)
	print(kilos[k])
	montecarlo(i, kilos[k])
	k = k + 1