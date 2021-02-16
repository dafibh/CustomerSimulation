class Csv_Import:
    def __init__(self):
        pass
    

    '''
        call this method to set columns before transferring csv into objects

        parameters:
        tStart  = Transaction Starting Row
        lStart  = Lines Starting Row
        tID     = Transaction ID column
        tDT     = Transaction Datetime column
        tCID    = Transaction Customer ID column

        tID2     = Transaction ID column in lines csv
        lIID    = Lines Item ID column
        lI      = Lines Item Name column
        lP      = Lines Price column

    '''
    def setColumns(self, tStart, lStart, tID, tDT, tCID, tID2, lIID, lI, lP):
        self.tStart = tStart # Transaction Starting Row
        self.lStart = lStart # Lines Starting Row
        
        # Transaction Columns
        self.tColumn = {
            "tid": tID,
            "datetime": tDT,
            "custid": tCID,
        }

        # Lines Columns
        self.lColumn = {
            "tid": tID2,
            "itemid": lIID,
            "item": lI,
            "price": lP,

        }


    def importcsv(self, transactionDir, linesDir):
        file = open(transactionDir, 'r') #transactions.csv
        contents = file.readlines()
        file.close()

        transaction = []
        lines = []

        contents = [line.strip() for line in contents[self.tStart:]]
        for line in contents:
            records = {
                "tid": "",
                "datetime": "",
                "custid": "",

            }

            data = line.split(',')
            records["tid"] = data[self.tColumn["tid"]]
            records["datetime"] = data[self.tColumn["datetime"]]
            records["custid"] = data[self.tColumn["custid"]]
            
            transaction.append(records)


        file = open(linesDir, 'r') #transactionslines.csv
        contents = file.readlines()
        file.close()

        contents = [line.strip() for line in contents[self.lStart:]]
        for line in contents:
            records = {
                "tid": "",
                "itemid": "",
                "item": "",
                "price": "",

            }

            data = line.split(',')
            records["tid"] = data[self.lColumn["tid"]]
            records["itemid"] = data[self.lColumn["itemid"]]
            records["item"] = data[self.lColumn["item"]]
            records["price"] = data[self.lColumn["price"]]
            
            lines.append(records)

        return transaction,lines