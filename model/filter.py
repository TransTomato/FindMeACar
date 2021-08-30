class Filter:
    priceR = [0, 500000000]
    title = ""
    location = ""
    yearRange = ""

    def __init__(self, priceR, title, location, yearR):
        self.priceR = priceR
        self.title = title
        self.location = location
        self.yearRange = str(yearR[0])+"-"+str(yearR[1])+"/"
    
    #Filters all the results using the user's input
    def dataFiltering(self,Cars):
        for c in Cars:
            for t in self.title.split(" "):
                if t not in c.title:
                    Cars.remove(c)
                    break
        return Cars
