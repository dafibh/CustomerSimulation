from datetime import datetime, timedelta
import pygame
from customer import Cust
from csvimport import readList
from transaction import Transactions

pygame.init()
clock = pygame.time.Clock()
win = pygame.display.set_mode((500,480))
pygame.display.set_caption("Pygame Test")


""" Set Images """
walkRight = []
walkRight.append(pygame.image.load('Prototype/Images/R1.png'))
walkRight.append(pygame.image.load('Prototype/Images/R2.png'))
walkRight.append(pygame.image.load('Prototype/Images/R3.png'))
walkRight.append(pygame.image.load('Prototype/Images/R4.png'))
walkRight.append(pygame.image.load('Prototype/Images/R5.png'))
walkRight.append(pygame.image.load('Prototype/Images/R6.png'))
walkRight.append(pygame.image.load('Prototype/Images/R7.png'))
walkRight.append(pygame.image.load('Prototype/Images/R8.png'))
walkRight.append(pygame.image.load('Prototype/Images/R9.png'))
bg = pygame.image.load('Prototype/Images/bg.jpg')
char = pygame.image.load('Prototype/Images/standing.png')
'''set Images end '''



""" Import CSV """
tcsv = []
lines = []
readList(tcsv, lines)

transaction = []

for i in tcsv:
    transaction.append(Transactions(i['tid'], i['datetime'], i['custid']))

for i in transaction:
    for j in lines:
        if j['lid'] == i.tid:
            i.add_Item(j)
""" Import csv end """



""" Set Sim Time """
start_time = datetime(2020, 7, 20, 8, 30) #set time

def addTime(): #add time function
    return start_time + timedelta(minutes=5)

def timestr(): #get time str
    timestring = str(start_time.strftime('%m/%d/%Y %I:%M %p'))

    if timestring[0] == "0":
        timestring = timestring[1:]
    return timestring
""" End Set Time """

test_time = datetime.strptime(timestr(), '%m/%d/%Y %I:%M %p')

a = test_time - timedelta(minutes=20)
test_time = a
print(f"test_time {test_time}")

"""
Test multiple

"""
rows = [0,64,128,192,256,320]

customer = []

"""
End Test multiple
"""



def redrawGameWindow(): #draw to screen
    
    win.blit(bg, (0,0))  

    checker = 0
    for cust in customer:
        if cust.x <= cust.dest:
            cust.move()
            win.blit(walkRight[cust.getStep()//3], (cust.x,cust.y))
        else:
            if cust.getStatus() == 2:
                cust.move()
                win.blit(walkRight[cust.getStep()//3], (cust.x,cust.y))
            else:
                win.blit(char, (cust.x, cust.y))
                if cust.getStatus() == 0:
                    cust.status = 1

        checker = checker + 1
    pygame.display.update() 



'''temp variables'''
start = 0    
seconds = 0



'''end temp variables'''


check = 0
transactiondone=0
print(f"time: {timestr()}")
run = True
while run:
    clock.tick(30)
    current_time = pygame.time.get_ticks() 

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_SPACE]:
        print(len(customer))

    if current_time <100:
        start = current_time

    if current_time - start >1000:
        start = current_time
        seconds = seconds + 1
        """print(seconds)"""
        start_time = addTime()
        print(f"time: {timestr()}")

        for cust in customer:
            if cust.getStatus() == 1 and cust.getWait() == 1:
                cust.status = 2
                print(f"Cust{cust.transaction.custid} done")
            elif cust.getStatus() == 1 and cust.getWait() == 0:
                cust.wait = 1

    for i in range(transactiondone,len(transaction)):

        if timestr() == transaction[i].get_Arrival() and len(customer)<=transactiondone:
            customer.append(Cust(0,rows[2],320,transaction[i]))
            #check = 1
            transactiondone = transactiondone + 1
        

    redrawGameWindow() 
    
    

pygame.quit()
