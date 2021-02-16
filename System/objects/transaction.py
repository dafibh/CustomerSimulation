class Transaction:
    def __init__(self,id):
        self.id = id
        self.date = ""
        self.time = ""
        self.custid = -1
        
    def setDate(self, d):
        self.date = d

    def setTime(self, t):
        self.time = t

    def setCustID(self, cID):
        self.custid = cID

    def getTime(self):
        return self.time

    def getDate(self):
        return self.date

    def getID(self):
        return self.id

    def getCustID(self):
        return self.custid

    def __repr__(self):
        return f"{self.id},{self.date} {self.time},{self.custid}"

    def getStr(self):
        return f"{self.id},{self.date} {self.time},{self.custid}"
        
    