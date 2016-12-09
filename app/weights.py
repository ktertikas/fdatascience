from pymongo import MongoClient
import numpy as np


def getConDict (  aaa ) :
	client = MongoClient('localhost',27017)
	db = client.fdatascience # create db name "fdatascience"
	s_con = db.consumption.find(aaa)
	con = []
	for i in s_con:
		con.append(i)
	mean_weights = []
	median_weights = []
	for i in con:
		median_weights.append(float(i["Median consumption in grams/ kg body weight per day"]))
		mean_weights.append(float(i["Mean consumption in grams/ kg body weight per day"]))
	x = np.array(mean_weights)
	y = np.array(median_weights)
	w_mean = np.true_divide(x, x.sum())
	w_median = np.true_divide(y, y.sum())

	# conc_coll = db.consumption_clean # create collection name "consumption_clean"

	f_con = []
	count_row=0
	for i in con:
		dic = {}
		dic["PopClass"] = i["Population Class"]
		dic["FoodName"] = i["Level 1 FoodEx Name"]
		dic["Mean"] = float(i["Mean consumption in grams/ kg body weight per day"])
		dic["MeanWeight"] = w_mean[count_row]
		dic["Median"] = float(i["Median consumption in grams/ kg body weight per day"])
		dic["MedianWeight"] = w_median[count_row]
		dic["Percentage"] = float(i["Percentage of consumers"])/100
		f_con.append(dic)
		count_row+=1
		# conc_coll.insert_one(dic)
	print(f_con)

def getBevDict (  aaa ) :
	client = MongoClient('localhost',27017)
	db = client.fdatascience # create db name "fdatascience"
	s_con = db.beverages_consumption.find(aaa)
	con = []
	for i in s_con:
		con.append(i)
	mean_weights = []
	median_weights = []
	for i in con:
		median_weights.append(float(i["Median consumption in grams/ kg body weight per day"]))
		mean_weights.append(float(i["Mean consumption in grams/ kg body weight per day"]))
	x = np.array(mean_weights)
	y = np.array(median_weights)
	w_mean = np.true_divide(x, x.sum())
	w_median = np.true_divide(y, y.sum())

	conc_coll = db.beverages_consumption_clean # create collection name "beverages_consumption_clean"

	f_con = []
	count_row=0
	for i in con:
		dic = {}
		dic["PopClass"] = i["Population Class"]
		dic["FoodName"] = i["Level 1 FoodEx Name"]
		dic["Mean"] = float(i["Mean consumption in grams/ kg body weight per day"])
		dic["MeanWeight"] = w_mean[count_row]
		dic["Median"] = float(i["Median consumption in grams/ kg body weight per day"])
		dic["MedianWeight"] = w_median[count_row]
		f_con.append(dic)
		count_row+=1
		# conc_coll.insert_one(dic)
	print(f_con)
