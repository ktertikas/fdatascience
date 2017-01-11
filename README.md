# Foundations of Data Science

#Abstract
Group 5

Idea: Are different age groups in the UK eating properly?
This is our first year in the UK, and one thing that caught our eye was that there is a huge amount of take aways, junk food restaurants, restaurants in general. So we are quite interested to know if people that live in the UK are in terms with the food guidelines that the NHS or the UK government provide to them. As a result, we are thinking of analysing the nutrient intakes of different age groups (children, adults, elderly people). By nutrient intakes we mean calories, proteins, carbohydrates, fats, vitamins, and all information that we can find, and try and make a correlation and see if people eat and drink as they should (using information from the NHS guidelines). 


#Guidelines

Infants:
https://wicworks.fns.usda.gov/wicworks/Topics/FG/Chapter1_NutritionalNeeds.pdf

Others:
https://www.gov.uk/government/uploads/system/uploads/attachment_data/file/547050/government__dietary_recommendations.pdf


#Installation Instructions

For anyone that wants to run the exact same analysis and server, please note first that your computer should have python3 installed, the libraries [numpy](http://www.numpy.org/), [matplotlib](http://matplotlib.org/), and [pymongo](https://api.mongodb.com/python/current/) as well as the [python tornado framework](http://www.tornadoweb.org/en/stable/). Finally, they should also have [mongoDB](https://www.mongodb.com/) installed.

After installing these libraries, in order to set the database and run the server, the following steps should be made:

1. Run file [import-data.py](https://github.com/ktertikas/fdatascience/blob/master/app/import-data.py)
2. Run file [analysis-test.py](https://github.com/ktertikas/fdatascience/blob/master/app/analysis-test.py)
3. Run file [nutrients-test.py](https://github.com/ktertikas/fdatascience/blob/master/app/nutrients-test.py)
4. Run file [final.py](https://github.com/ktertikas/fdatascience/blob/master/app/final.py)
5. Run [server.py](https://github.com/ktertikas/fdatascience/blob/master/app/server.py)
