from datetime import datetime, timedelta
import pygame
from modules.customer_anim import Customer_Anim
from modules.transaction_anim import Transaction_Anim

class Simulation:
    def __init__(self, controller):
        self.controller = controller
        self.start = 0    
        self.seconds = 0
        self.check = 0
        self.transactiondone=0
        self.tickamount=30
        self.testtime = 1000
        self.speed = 1

    def startSim(self,tlist,llist):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.win = pygame.display.set_mode((500,480))
        pygame.display.set_caption("Customer Simulation System")

        self.walkRight = []
        self.walkRight.append(pygame.image.load('../CustomerSimulation/System/assets/images/R1.png'))
        self.walkRight.append(pygame.image.load('../CustomerSimulation/System/assets/images/R2.png'))
        self.walkRight.append(pygame.image.load('../CustomerSimulation/System/assets/images/R3.png'))
        self.walkRight.append(pygame.image.load('../CustomerSimulation/System/assets/images/R4.png'))
        self.walkRight.append(pygame.image.load('../CustomerSimulation/System/assets/images/R5.png'))
        self.walkRight.append(pygame.image.load('../CustomerSimulation/System/assets/images/R6.png'))
        self.walkRight.append(pygame.image.load('../CustomerSimulation/System/assets/images/R7.png'))
        self.walkRight.append(pygame.image.load('../CustomerSimulation/System/assets/images/R8.png'))
        self.walkRight.append(pygame.image.load('../CustomerSimulation/System/assets/images/R9.png'))
        self.bg = pygame.image.load('../CustomerSimulation/System/assets/images/bg.jpg')
        self.char = pygame.image.load('../CustomerSimulation/System/assets/images/standing.png')
        self.counter = pygame.image.load('../CustomerSimulation/System/assets/images/counter.png')
        self.counter = pygame.transform.scale(self.counter, (72, 70))

        

        self.font = pygame.font.SysFont(None , 25)
        self.timetext = self.font.render("",True,(0,0,0))
        self.logtitle = self.font.render("-- Log --",True,(0,0,0))
        self.logtext = self.font.render("",True,(0,0,0))
        self.itemtext = []
        self.itemtext.append(self.font.render("",True,(0,0,0)))
        self.itemtext.append(self.font.render("",True,(0,0,0)))
        self.itemtext.append(self.font.render("",True,(0,0,0)))
        self.itemtext.append(self.font.render("",True,(0,0,0)))
        self.itemtext.append(self.font.render("",True,(0,0,0)))

        self.rows = [0,64,128,192,256,320]

        self.tDictList = tlist
        self.lDictList = llist
        self.customer = []
        self.transactions = []
        self.setTransactionObjects()
        self.run()

    def redrawGameWindow(self): #draw to screen
    
        self.win.blit(self.bg, (0,0)) #draw background
        self.win.blit(self.timetext, (20,20)) #draw time text
        #self.win.blit(self.logtitle, (20,260)) #draw log title text
        self.win.blit(self.logtext, (20,280)) #draw log text
        self.win.blit(self.counter, (350,self.rows[3])) #draw.counter
        #self.win.blit(self.counter, (350,self.rows[1])) #draw.counter 1
        #self.win.blit(self.counter, (350,self.rows[5])) #draw.counter 3

        self.win.blit(self.itemtext[0], (20,320)) #draw log text
        self.win.blit(self.itemtext[1], (20,340)) #draw log text
        self.win.blit(self.itemtext[2], (20,360)) #draw log text
        self.win.blit(self.itemtext[3], (20,380)) #draw log text
        self.win.blit(self.itemtext[4], (20,400)) #draw log text

        checker = 0
        for cust in self.customer:
            if cust.x <= cust.dest:
                if self.pause == False:
                    cust.move()
                self.win.blit(self.walkRight[cust.getStep()//3], (cust.x,cust.y))
            else:
                if cust.getStatus() == 2:
                    if self.pause == False:
                        cust.move()
                    self.win.blit(self.walkRight[cust.getStep()//3], (cust.x,cust.y))
                else:
                    self.win.blit(self.char, (cust.x, cust.y))
                    if cust.getStatus() == 0:
                        cust.status = 1

            checker = checker + 1
        
        pygame.display.update()



    def run(self):
        #convert json first before running
        #self.setTransactionObjects(json)

        self.controller.frames["SimPage"].clearLog()
        running = True
        self.pause = False
        self.tick = 0

        while running == True:
            self.clock.tick(self.tickamount)

            

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.MOUSEBUTTONUP:
                    if len(self.customer)>0:
                        for i in self.customer:
                            if i.status != 2:
                                if i.isCollide(pygame.mouse.get_pos()):
                                    self.controller.frames["SimPage"].clearInventory()
                                    print(f"\n\n--Customer ID {i.transaction.custid} items--")
                                    total = 0
                                    for j in i.transaction.items:
                                        self.controller.frames["SimPage"].addInventory(f"RM {j['price']} - {j['item']}")
                                        total = total + float(j['price'])
                                    self.controller.frames["SimPage"].addInventory("Total : RM %.2f" % round(total, 2))

            self.keys = pygame.key.get_pressed()
                
            if self.keys[pygame.K_SPACE]:
                #self.controller.show_frame("Admin_Options")
                self.setTimeText("hello")

                

            if self.pause == False:
                self.current_time = pygame.time.get_ticks() 
                """self.tick = self.tick+1
                if self.tick%30 == 0: #do something every second
                    self.controller.frames["SimPage"].addItem(self.tick/30) #add item to log box"""

                if self.current_time <100:
                    self.start = self.current_time

                #if current_time - start >1000:
                if self.current_time - self.start >self.testtime:
                    self.start = self.current_time
                    """ Update time """
                    self.start_time = self.addTime()
                    self.timetext = self.font.render(self.timestr(),True,(0,0,0))
                    

                    for cust in self.customer:
                        if cust.getStatus() == 1 and cust.getWait() == 1:
                            cust.status = 2
                            #logtext = font.render(f"Customer ID {cust.transaction.custid} completed transaction",True,(0,0,0))
                            self.controller.frames["SimPage"].addItem(f"Customer ID {cust.transaction.custid} completed transaction")
                            #self.controller.frames["SimPage"].addItem(f"T_ID: {cust.transaction.custid} | C")

                            #Empty Text
                            #itemtext[0] = font.render("",True,(0,0,0))
                            #itemtext[1] = font.render("",True,(0,0,0))
                            #itemtext[2] = font.render("",True,(0,0,0))
                            #itemtext[3] = font.render("",True,(0,0,0))
                            #itemtext[4] = font.render("",True,(0,0,0))

                            #for j in range(len(cust.transaction.items)): # set item text
                                #self.itemtext[j] = self.font.render(f"[{j+1}] {cust.transaction.items[j]['item']} ---  RM {cust.transaction.items[j]['price']} ",True,(0,0,0))
                                

                        elif cust.getStatus() == 1 and cust.getWait() == 0:
                            cust.wait = 1


                for i in range(self.transactiondone,len(self.transactions)):
                    if self.timestr() == self.transactions[i].get_Arrival() and len(self.customer)<=self.transactiondone:
                        self.customer.append(Customer_Anim(0,self.rows[2],320,self.transactions[i]))
                        self.transactiondone = self.transactiondone + 1

            
            self.redrawGameWindow()            
        pygame.quit()




    def setTransactionObjects(self):
        
        #transfer from dictionary to regular objects

        for i in self.tDictList:
            self.transactions.append(Transaction_Anim(i['tid'], i['datetime'], i['custid']))

        for i in self.transactions:
            for j in self.lDictList:
                if j["tid"] == i.tid:
                    i.add_Item(j)

        self.controller.frames["SimPage"].setTransactionObjects(self.transactions)
        
        
        #set starting time from first transaction, minus 1 hour
        a = datetime.strptime(self.tDictList[0]["datetime"], '%m/%d/%Y %I:%M %p')
        b = a - timedelta(minutes=30)

        self.start_time = datetime(b.year, b.month, b.day, b.hour, b.minute)

        print(f"STARTING time: {self.start_time}")

        for i in self.transactions:
            print(i)

        for i in self.transactions:
            print(f"Customer {i.tid} items")
            for j in i.items:
                print(f"item name: {j['item']} | item price {j['price']}")



    def addTime(self): #add time function
        return self.start_time + timedelta(minutes=5)

    def timestr(self): #get time str
        timestring = str(self.start_time.strftime('%m/%d/%Y %I:%M %p'))

        if timestring[0] == "0":
            timestring = timestring[1:]
        return timestring

    def setTimeText(self, x):
        self.timetext = self.font.render(x,True,(0,0,0))

    def quitWindow(self):
        pygame.quit()
        print("test")

    def playPauseToggle(self):
        if self.pause == True:
            self.pause = False
        else:
            self.pause = True

    def backward(self):
        self.tickamount=self.tickamount/2
        self.testtime=self.testtime*2
        self.speed = self.speed / 2

    def forward(self):
        if self.speed< 32 and self.speed != 16:
            self.tickamount=self.tickamount*2
            self.testtime=self.testtime/2
            self.speed = self.speed * 2

    def save(self):
        pass

