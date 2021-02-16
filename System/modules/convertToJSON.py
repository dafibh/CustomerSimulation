from tinydb import TinyDB
class Converter:
    def __init__(self):
        pass


    def convert(self, transactionlist, linelist):
        json = {}
        json["transactions"] = transactionlist
        json["lines"] = linelist
        return json