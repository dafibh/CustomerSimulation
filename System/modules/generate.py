from objects.customer import Customer
from objects.transaction import Transaction
from objects.transactionline import Transaction_Lines
import random
from datetime import datetime, timedelta
from tkinter import filedialog
import math

class Record_Generator:
    def __init__(self,controller):
        self.controller = controller

    def generate(self):
        print("Generating...")

        # customer parameters
        custN = self.controller.customerAmount 
        custTypeN = self.controller.customerTypesN 
        custTypePurchases = []
        custTypeReturns = []

        customerList = []        

        custTypePurchases.append(int(self.controller.customerTypes["t1P"]))
        custTypePurchases.append(int(self.controller.customerTypes["t2P"]))
        custTypePurchases.append(int(self.controller.customerTypes["t3P"]))

        custTypeReturns.append(int(self.controller.customerTypes["t1R"]))
        custTypeReturns.append(int(self.controller.customerTypes["t2R"]))
        custTypeReturns.append(int(self.controller.customerTypes["t3R"]))

        # product parameters
        productsN = len(self.controller.productList)
        productsList = self.controller.productList
        
        # store parameters
        startHour = self.controller.storeStartHour
        endHour = self.controller.storeCloseHour
        workingDays = self.controller.storeOperationDays

        # generation parameters
        daysToSimulate = self.controller.generationDays
        startingDate = self.controller.generationStartingDate
        genType = self.controller.generationCustomerDistribution # this is for within the day, means distribute evenly between dates, but normally between the time

        # create customers

        for i in range(custN):
            customerList.append(Customer(i))

        for i in customerList:
            # give type to customer
            ctype = random.randint(1, custTypeN)

            # set purchase N
            i.setPurchaseN(custTypePurchases[ctype-1])

            # set returning
            i.setReturning(custTypeReturns[ctype-1])



        # create transaction Objects

        transactionN = 0
        transactionList = []

        for i in customerList:
            transactionN += i.getReturning()

        for i in range(transactionN):
            transactionList.append(Transaction(i))

        # assigning customers to transactions

        transactionLottery = []
        for i in range(transactionN):
            transactionLottery.append(i)

        for i in customerList:
            for j in range(i.getReturning()):
                transactionList[transactionLottery.pop(random.randint(0,len(transactionLottery)-1))].setCustID(i.getID())

        # customer id and transaction id in transaction object has been set
        # create transaction line objects

        transactionLinesList = []

        for i in transactionList:
            for j in range(customerList[i.getCustID()].getPurchaseN()):
                # choose random product
                prod = productsList[random.randint(0,productsN-1)]
                
                # append new line
                transactionLinesList.append(Transaction_Lines(i.getID(),prod.getID(),f"{prod.getBrand()} {prod.getName()}", prod.getPrice()))

        

        #-----------------------------------------------------------------------------------------------------------------------------
        # assigning dates to transactions                                                       REVAMP, USE FORMULA

        daysProcessed = 0
        datecomponents = startingDate.split("/")
        startDate = datetime(int(datecomponents[2])+2000, int(datecomponents[0]), int(datecomponents[1]))
        day_name = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday','Sunday']

        workingDatesList = []
        
        while daysProcessed < int(daysToSimulate):
            datestr = str(startDate.strftime('%m/%d/%Y'))
            weekdayindicator = datetime.strptime(datestr, '%m/%d/%Y').weekday()

            if day_name[weekdayindicator] in workingDays:
                workingDatesList.append(str(startDate.strftime('%m/%d/%Y')))
                daysProcessed += 1
            startDate += timedelta(days=1)


        transtodatescheck = []

        for i in range(transactionN): #transfer the transaction into a checking variable
            transtodatescheck.append(i)


        transactionPerDay = -(-transactionN//int(daysToSimulate))


        if genType == "Exponential":
            #do expo
            a = 0.9
            b = 1.2 #steepness, lower if the angle is too steep, 1.0 is basically uniform distribution
            c = 0

            transactionAmount = transactionN
            days = int(daysToSimulate)
            steps = 10/days

            x = 1

            rawWeights = []

            for i in range(days):
	            #y = (1/(a*math.sqrt(2*3.14)))*math.exp(-(((x-b)*(x-b))/(2*a*a))) #formula for a normal distributed graph
	            y = (a*(b**(-6+x))) + c
	            rawWeights.append(y)
	            x = x + steps

            weights = []

            for i in rawWeights:
	            weights.append(i/sum(rawWeights))

            tperDay = [] #appending rounded number of those weight, basically how many transaction per day
            for i in weights:
	            tperDay.append(round((i/sum(weights))*transactionAmount))

            

            #assign dates here ------------------------------------------

            counter = [] #counter for how many transactions have been assign dates
            for i in range(len(tperDay)):
                counter.append(0)

            c=0
            for i in workingDatesList:
                
                while counter[c]<tperDay[c] and len(transtodatescheck) > 0:
                    #put date in transaction
                    transactionList[transtodatescheck.pop(0)].setDate(i)
                    counter[c] = counter[c]+1
                
                c = c+1


            
            
        elif genType == "Normal":
            #do normal
            a = 1
            b = 4 #midpoint of graph

            transactionAmount = transactionN
            days = int(daysToSimulate)
            steps = 6/days
            x = 1 #starting point of normal dist graph

            rawWeights = [] #raw number of weight eg 0.858474857, we will turn them into normal weight over 1, basically probability

            for i in range(days): #assigning those raw weights, based on pre set graph of normal dist, we find the value of y(density) for each step of x(variable)
	            y = (1/(a*math.sqrt(2*3.14)))*math.exp(-(((x-b)*(x-b))/(2*a*a))) #formula for a normal distributed graph
	            rawWeights.append(y)
	            x = x + steps

            weights = [] # normal weights or probability, basically (raw weights over total of raw weights). the sum of weight will be as close as possible to 1.0
            for i in rawWeights:
	            weights.append(i/sum(rawWeights))

            tperDay = [] #appending rounded number of those weight, basically how many transaction per day
            for i in weights:
	            tperDay.append(round((i/sum(weights))*transactionAmount))

            #assign dates here ------------------------------------------

            counter = [] #counter for how many transactions have been assign dates
            for i in range(len(tperDay)):
                counter.append(0)

            c=0
            for i in workingDatesList:
                
                while counter[c]<tperDay[c] and len(transtodatescheck) > 0:
                    #put date in transaction
                    transactionList[transtodatescheck.pop(0)].setDate(i)
                    counter[c] = counter[c]+1
                
                c = c+1

        else:
            #do uniform 
            a = 0.9
            b = 1 #steepness, lower if the angle is too steep, 1.0 is basically uniform distribution
            c = 0

            transactionAmount = transactionN
            days = int(daysToSimulate)
            steps = 10/days

            x = 1

            rawWeights = []

            for i in range(days):
	            #y = (1/(a*math.sqrt(2*3.14)))*math.exp(-(((x-b)*(x-b))/(2*a*a))) #formula for a normal distributed graph
	            y = (a*(b**(-6+x))) + c
	            rawWeights.append(y)
	            x = x + steps

            weights = []

            for i in rawWeights:
	            weights.append(i/sum(rawWeights))

            tperDay = [] #appending rounded number of those weight, basically how many transaction per day
            for i in weights:
	            tperDay.append(round((i/sum(weights))*transactionAmount))

            

            #assign dates here ------------------------------------------

            counter = [] #counter for how many transactions have been assign dates
            for i in range(len(tperDay)):
                counter.append(0)

            c=0
            for i in workingDatesList:
                
                while counter[c]<tperDay[c] and len(transtodatescheck) > 0:
                    #put date in transaction
                    transactionList[transtodatescheck.pop(0)].setDate(i)
                    counter[c] = counter[c]+1
                
                c = c+1


        

        #-------------------------------------------------------------------------------------------------------------------------------
        # assigning time to transactions                                                            #REVAMP DO UNIFORM
        # using chosen formula (uniform, normal, exponential)

        # declaring available timeslots

        workingTime = []

        start = datetime(int(datecomponents[2])+2000, int(datecomponents[0]), int(datecomponents[1]),int(startHour),0)
        end = datetime(int(datecomponents[2])+2000, int(datecomponents[0]), int(datecomponents[1]),int(endHour),0)

        timestr1 = str(start.strftime('%I:%M %p'))
        timestr2 = str(end.strftime('%I:%M %p'))

        while timestr1 != timestr2:
            workingTime.append(timestr1)
            start += timedelta(minutes=10)
            timestr1 = str(start.strftime('%I:%M %p'))

        # based on formula choose stuff



        sectionsN = len(workingTime)
        tSteps = []
        for i in range(len(tperDay)):
            if sectionsN/(tperDay[i]+1)<1:
                tSteps.append(1)
            else:
                tSteps.append(int(math.floor(sectionsN/(tperDay[i]+1))))
            
        
        pointer = 0
        prevdate = transactionList[0].getDate()

        tstepscounter = 0
        for i in transactionList:
            if tSteps[tstepscounter] >= sectionsN:
                tstepscounter = tstepscounter+1
            if prevdate != i.getDate() or pointer >= sectionsN:
                pointer = 0
                tstepscounter = tstepscounter + 1

            
            i.setTime(workingTime[pointer])
            if tstepscounter < len(tSteps):
                pointer += tSteps[tstepscounter]
            prevdate = i.getDate()    
        
                
        
        # prompt save directory
        chosenDir = filedialog.askdirectory()

        # create new file and write to, not append, use w
        transactionText = ""
        linesText = ""

        #transaction header
        transactionText += "[0]-transactionID, [1]-datetime, [2]-customerID"
        transactionText += "\n"

        for i in transactionList:
            transactionText += i.getStr()
            transactionText += "\n"

        #lines header
        linesText += f"[0]-linesID, [1]-transactionID, [2]-productID, [3]-productName, [4]-productPrice"
        linesText += "\n"

        for i in range(len(transactionLinesList)):
            linesText += f"{i},{transactionLinesList[i].getStr()}"
            linesText += "\n"


        
        f = open(f"{chosenDir}/transactions.csv", "w")
        f.write(transactionText)
        f.close()

        f = open(f"{chosenDir}/transactionLines.csv", "w")
        f.write(linesText)
        f.close()

        
