class Car:
    price = 0
    title = ""
    location = ""
    year = ""
    link = ""

    def __init__(self, price, title, location, year, link):
        self.price = price
        self.title = title
        self.location = location
        self.year = year
        self.link = link

    def __repr__(self):
        return "Precio: "+str(self.price)+"\nTitulo: "+self.title+"\nUbicacion: "+self.location+"ano: "+self.year+"\nLink: "+self.link