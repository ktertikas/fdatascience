from pymongo import MongoClient
import numpy as np


def getNutr (  aaa ) :
	client = MongoClient('localhost',27017)
	db = client.fdatascience # create db name "fdatascience"
	s_con = db.nutrients.find(aaa)
	con = []
	for i in s_con:
		con.append(i)

	f_con = []
	count_row=0
	for i in con:
		dic = {}
		dic["FoodCode"] = i["Food Code"]
		dic["FoodName"] = i["Food Name"]
		dic["Group"] = i["Group"]
		dic["Water"] = float(i["Water (g)"])
		dic["Nitrogen"] = float(i["Total nitrogen (g)"])
		dic["Protein"] = float(i["Protein (g)"])
		dic["Fat"] = float(i["Fat (g)"])
		dic["Carbohydrate"] = float(i["Carbohydrate (g)"])
		dic["EnergyCal"] = float(i["Energy (kcal) (kcal)"])
		dic["EnergyJ"] = float(i["Energy (kJ) (kJ)"])
		dic["Sugars"] = float(i["Total sugars (g)"])
		dic["Glucose"] = float(i["Glucose (g)"])
		dic["Sucrose"] = float(i["Sucrose (g)"])
		dic["Lactose"] = float(i["Lactose (g)"])
		dic["Cholesterol"] = float(i["Cholesterol (mg)"])
		dic["VitaminD"] = float(i["Vitamin D (µg)"])
		dic["VitaminE"] = float(i["Vitamin E (mg)"])
		dic["VitaminK"] = float(i["Vitamin K1 (µg)"])
		dic["VitaminB6"] = float(i["Vitamin B6 (mg)"])
		dic["VitaminB12"] = float(i["Vitamin B12 (µg)"])
		dic["VitaminC"] = float(i["Vitamin C (mg)"])
		f_con.append(dic)
		count_row+=1
	print(f_con)
