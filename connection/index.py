#authors Michelle Quintero Hernandez

#Setting path
import sys
sys.path.insert(0, './')

from selenium import webdriver
from model.car import Car

#Search elements declarations
car = "renault-12"
indexNum = 0
index = "Desde_"+str(48*indexNum+1)
sort = "OrderId_PRICE"
pRange = [0,12000000]
priceRange = "PriceRange_"+str(pRange[0])+"-"+str(pRange[1])
yRange = ["hasta","1992"]
yearRange = str(yRange[0])+"-"+str(yRange[1])+"/"

# create webdriver object
driver = webdriver.Firefox()

# get carros.mercadolibre.com.co
driver.get("https://carros.mercadolibre.com.co/"+yearRange+car+"_"+index+"_"+sort+"_"+priceRange)

#get results
results = driver.find_elements_by_class_name("ui-search-layout__item")

#Adding results
cars = list()
for r in results:
    price = int(r.find_element_by_class_name("price-tag-fraction").text.replace(".",""))
    #title = r.find_element_by_class_name("ui-search-item__title ui-search-item__group__element").text
    #location = r.find_element_by_class_name("ui-search-item__group__element ui-search-item__location").text
    year = r.find_element_by_class_name("ui-search-card-attributes__attribute").text
    title = "title"
    location = "location"
    #year = "year"


    car = Car(price,title,location,year)
    cars.append(car)

print(cars[0].price)

    