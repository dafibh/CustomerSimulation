class Products:
    def __init__(self, id, name, brand, price):
        self.id = id
        self.name = name
        self.brand = brand
        self.price = price

    def getID(self):
        return self.id

    def getName(self):
        return self.name

    def getBrand(self):
        return self.brand

    def getPrice(self):
        return self.price


    def setName(self,name):
        self.name = name

    def setPrice(self,price):
        self.price = price

    def setBrand(self,brand):
        self.brand = brand

    def __repr__(self):
        return f"{{id}}: {self.id} | {{name}}: {self.name} | {{brand}}: {self.brand} | {{price}}: {self.price}"