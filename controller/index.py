#authors Michelle Quintero Hernandez
# import webdriver
from selenium import webdriver
#from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

#Search elements declarations
car = "renault-4"
indexNum = 0
index = "Desde_"+str(48*indexNum+1)
sort = "OrderId_PRICE"
pRange = [0,10000000]
priceRange = "PriceRange_"+str(pRange[0])+"-"+str(pRange[1])
yRange = ["hasta","1992"]
yearRange = str(yRange[0])+"-"+str(yRange[1])+"/"

# create webdriver object
driver = webdriver.Firefox()

# get carros.mercadolibre.com.co
driver.get("https://carros.mercadolibre.com.co/"+yearRange+car+"_"+index+"_"+sort+"_"+priceRange)

#get results
results = driver.find_elements_by_class_name("ui-search-layout__item")

for r in results:
    print("si")