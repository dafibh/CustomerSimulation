def readList(transaction, lines):
    file = open('Prototype/transactions.csv', 'r') #transactions.csv
    contents = file.readlines()
    file.close()

    contents = [line.strip() for line in contents[0:]]
    for line in contents:
        records = {
            "tid": "",
            "datetime": "",
            "custid": "",

        }

        data = line.split(',')
        records["tid"] = data[0]
        records["datetime"] = data[1]
        records["custid"] = data[3]
        
        transaction.append(records)


    file = open('Prototype/transactionlines.csv', 'r') #transactionslines.csv
    contents = file.readlines()
    file.close()

    contents = [line.strip() for line in contents[0:]]
    for line in contents:
        records = {
            "lid": "",
            "datetime": "",
            "quantity": "",
            "item": "",
            "price": "",

        }

        data = line.split(',')
        records["lid"] = data[0]
        records["datetime"] = data[2]
        records["quantity"] = data[3]
        records["item"] = data[4]
        records["price"] = data[5]
        
        lines.append(records)

    #for i in lines:
        #print(i)