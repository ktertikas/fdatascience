from pymongo import MongoClient
import numpy as np

# Function to clean all data in the collection "nutrients"
# and create the new collection "nutrients_clean"
def getNutr ( foodcode ) :
	client = MongoClient('localhost',27017)
	db = client.fdatascience # create db name "fdatascience"
	s_con = db.nutrients.find(foodcode)
	con = []
	for i in s_con:
		con.append(i)

	nuc_coll = db.nutrients_clean # create collection name "nutrients_clean"
	f_con = []
	for i in con:
		dic = {}
		dic["FoodCode"] = i["Food Code"]
		dic["FoodName"] = i["Food Name"]
		dic["Group"] = i["Group"]
		if i["Water (g)"]: 
			dic["Water"] = float(i["Water (g)"])
		if i["Total nitrogen (g)"]: 
			dic["Nitrogen"] = float(i["Total nitrogen (g)"])
		if i["Protein (g)"]: 
			dic["Protein"] = float(i["Protein (g)"])
		if i["Fat (g)"]: 
			dic["Fat"] = float(i["Fat (g)"])
		if i["Carbohydrate (g)"]: 
			dic["Carbohydrate"] = float(i["Carbohydrate (g)"])
		if i["Energy (kcal) (kcal)"]: 
			dic["EnergyCal"] = float(i["Energy (kcal) (kcal)"])
		if i["Energy (kJ) (kJ)"]: 
			dic["EnergyJ"] = float(i["Energy (kJ) (kJ)"])
		if i["Total sugars (g)"]: 
			dic["Sugars"] = float(i["Total sugars (g)"])
		if i["Glucose (g)"]: 
			dic["Glucose"] = float(i["Glucose (g)"])
		if i["Sucrose (g)"]: 
			dic["Sucrose"] = float(i["Sucrose (g)"])
		if i["Lactose (g)"]: 
			dic["Lactose"] = float(i["Lactose (g)"])
		if i["Cholesterol (mg)"]: 
			dic["Cholesterol"] = float(i["Cholesterol (mg)"])
		if i["Vitamin D (µg)"]: 
			dic["VitaminD"] = float(i["Vitamin D (µg)"])
		if i["Vitamin E (mg)"]: 
			dic["VitaminE"] = float(i["Vitamin E (mg)"])
		if i["Vitamin K1 (µg)"]: 
			dic["VitaminK"] = float(i["Vitamin K1 (µg)"])
		if i["Vitamin B6 (mg)"]: 
			dic["VitaminB6"] = float(i["Vitamin B6 (mg)"])
		if i["Vitamin B12 (µg)"]: 
			dic["VitaminB12"] = float(i["Vitamin B12 (µg)"])
		if i["Vitamin C (mg)"]: 
			dic["VitaminC"] = float(i["Vitamin C (mg)"])
		f_con.append(dic)
		print(dic)
		nuc_coll.insert_one(dic)
	# print(f_con)
