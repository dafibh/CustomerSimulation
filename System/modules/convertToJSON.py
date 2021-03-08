from tinydb import TinyDB
class Converter:
    def __init__(self):
        pass


    def convert(self, transactionlist, linelist, time):
        json = {}
        json["transactions"] = transactionlist
        json["lines"] = linelist
        json["time"] = time
        return json