class Transaction_Lines:
    def __init__(self,transID, productID, productName, productPrice):
        self.transID = transID
        self.productID = productID
        self.productName = productName
        self.productPrice = productPrice

    def __repr__(self):
        return f"{self.transID},{self.productID},{self.productName},{self.productPrice}"

    def getStr(self):
        return f"{self.transID},{self.productID},{self.productName},{self.productPrice}"