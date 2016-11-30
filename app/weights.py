from pymongo import MongoClient
import numpy as np

def getDict ( aaa ) :
	mean_weights_inf = []
	median_weights_inf = []
	for i in aaa:
		median_weights_inf.append(float(i["Median consumption in grams/ kg body weight per day"]))
		mean_weights_inf.append(float(i["Mean consumption in grams/ kg body weight per day"]))
	x = np.array(mean_weights_inf)
	y = np.array(median_weights_inf)
	w_mean_inf = np.true_divide(x, x.sum())
	w_median_inf = np.true_divide(y, y.sum())
