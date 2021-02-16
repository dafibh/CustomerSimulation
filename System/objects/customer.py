class Customer:
    def __init__(self, id):
        self.purchaseN = 1
        self.returning = 1
        self.ID = id

    def setPurchaseN(self, pN):
        self.purchaseN = pN
    
    def setReturning(self, r):
        self.returning = r
    
    def getPurchaseN(self):
        return self.purchaseN

    def getReturning(self):
        return self.returning

    def getID(self):
        return self.ID

    def __repr__(self):
        return f"CustID = {self.ID} | pN = {self.purchaseN} | returning = {self.returning}"