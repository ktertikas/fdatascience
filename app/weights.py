from pymongo import MongoClient
import numpy as np

# Function to clean all data in the collection "consumption"
# and create the new collection "consumption_clean"
def getConDict ( s_popclass ) :
	client = MongoClient('localhost',27017)
	db = client.fdatascience
	s_con = db.consumption.find(s_popclass)
	con = []
	for i in s_con:
		con.append(i)
	mean_weights = []
	median_weights = []
	# calculate mean and median weights consumption for population class
	for i in con:
		median_weights.append(float(i["Median consumption in grams/ kg body weight per day"]))
		mean_weights.append(float(i["Mean consumption in grams/ kg body weight per day"]))
	x = np.array(mean_weights)
	y = np.array(median_weights)
	w_mean = np.true_divide(x, x.sum())
	w_median = np.true_divide(y, y.sum())

	conc_coll = db.consumption_clean # create collection name "consumption_clean"
	f_con = []
	count_row=0
	# add for every population class the following appropriate key value pairs
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
		conc_coll.insert_one(dic) # insert the clean data into the new collection "consumption_clean"
	print(f_con)
