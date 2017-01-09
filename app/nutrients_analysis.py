from pymongo import MongoClient
import numpy as np
import json
import matplotlib.pyplot as plt

client = MongoClient('localhost',27017)
db = client.fdatascience
nutrc_foodcode = db.nutrients_clean.distinct("FoodCode")
nutr_keys = ['VitaminC', 'Fat', 'VitaminK', 'Nitrogen', 'Cholesterol', 'EnergyJ', 'VitaminD', 'Glucose', 'Protein', 'Sugars', 'Carbohydrate', 'VitaminB12', 'VitaminE', 'Lactose', 'Sucrose', 'VitaminB6', 'Water', 'EnergyCal']
nutr_texts = ['Vitamin C', 'Fat', 'Vitamin K1', 'Nitrogen', 'Cholesterol', 'Energy J', 'Vitamin D', 'Glucose', 'Protein', 'Sugars', 'Carbohydrate', 'Vitamin B12', 'Vitamin E', 'Lactose', 'Sucrose', 'Vitamin B6', 'Water', 'Energy Cal']
nutr_units = ['mg', 'g', 'µg', 'g', 'mg', 'kJ', 'µg', 'g', 'g', 'g', 'g', 'µg', 'mg', 'g', 'g', 'mg', 'g', 'kcal']
final=[]
for i in nutrc_foodcode:
	file = open("nutrients_text_output/"+i+".txt", "wb")
	dic={}
	count_texts = 0
	for j in nutr_keys:
		nutr_key_value = db.nutrients_clean.find( {j:{'$ne':None}, "FoodCode":i}, {'_id':0, j:1} )
		temp = np.array([])
		for k in nutr_key_value:
			temp = np.append(temp, k[j])
		if len(temp) != 0:
			print("Food Code in processing: "+i+" & Key->"+j)
			# Draw Histogram
			plt.hist(temp, bins=20)
			plt.suptitle(i+" ("+nutr_texts[count_texts]+")")
			plt.xlabel(nutr_texts[count_texts]+" ("+nutr_units[count_texts]+")")
			plt.ylabel('Number of items')
			plt.savefig('nutrients_graphical_output/'+i+'_'+j+'.png')
			plt.clf()

			# Draw Boxplot
			plt.boxplot(temp)
			plt.suptitle(i+" ("+nutr_texts[count_texts]+")")
			plt.tick_params(axis='both', left='on', top='off', right='off', bottom='off', labelleft='on', labeltop='off', labelright='off', labelbottom='off')
			plt.ylabel(nutr_texts[count_texts]+" ("+nutr_units[count_texts]+")")
			plt.savefig('nutrients_graphical_output/boxplot_'+i+'_'+j+'.png')
			plt.clf()

			# Print Text
			mean_print = "mean value of "+j+" is ;"+str(np.mean(temp))
			median_print = "median value of "+j+" is ;"+str(np.median(temp))
			sd_print = "standard deviation value of "+j+" is ;"+str(np.std(temp))
			file.write(mean_print.encode('utf-8'))
			file.write(b"\n")
			file.write(median_print.encode('utf-8'))
			file.write(b"\n")
			file.write(sd_print.encode('utf-8'))
			file.write(b"\n")

		count_texts = count_texts+1
		# Get only one nutrient (EnergyCal)
		if j == "EnergyCal":
			dic["FoodCode"] = i
			dic[j] = np.median(temp)
	final.append(dic)
	file.close()
print(final)

# Find clean consumption for infants and take median weights for every food group
consum = db.consumption_clean.find({"PopClass":"Infants"})
for i in consum:
	sum1 = 0
	for j in final:
		if i["FoodName"] == j["FoodCode"]:
			# print(i["MedianWeight"])
			# print(j["EnergyCal"])
			sum1 = sum1 + i["MedianWeight"] * j["EnergyCal"]
print(sum1)
			