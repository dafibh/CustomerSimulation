from datetime import datetime, timedelta
import pygame
from customer import Cust
from csvimport import readList
from transaction import Transactions

pygame.init()
clock = pygame.time.Clock()
win = pygame.display.set_mode((500,480))
pygame.display.set_caption("Prototype Test")


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
counter = pygame.image.load('Prototype/Images/counter.png')
counter = pygame.transform.scale(counter, (72, 70))
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



""" Text on screen """
font = pygame.font.SysFont(None , 25)
timetext = font.render("",True,(0,0,0))
logtitle = font.render("-- Log --",True,(0,0,0))
logtext = font.render("",True,(0,0,0))
itemtext = []
itemtext.append(font.render("",True,(0,0,0)))
itemtext.append(font.render("",True,(0,0,0)))
itemtext.append(font.render("",True,(0,0,0)))
itemtext.append(font.render("",True,(0,0,0)))
itemtext.append(font.render("",True,(0,0,0)))

def setTimeText(x):
    timetext = font.render(x,True,(0,0,0))


""" End Text on Screen """



"""
Test multiple

"""
rows = [0,64,128,192,256,320]

customer = []

"""
End Test multiple
"""



def redrawGameWindow(): #draw to screen
    
    win.blit(bg, (0,0)) #draw background
    win.blit(timetext, (20,20)) #draw time text
    win.blit(logtitle, (20,260)) #draw log title text
    win.blit(logtext, (20,280)) #draw log text
    win.blit(counter, (350,rows[3])) #draw.counter

    win.blit(itemtext[0], (20,320)) #draw log text
    win.blit(itemtext[1], (20,340)) #draw log text
    win.blit(itemtext[2], (20,360)) #draw log text
    win.blit(itemtext[3], (20,380)) #draw log text
    win.blit(itemtext[4], (20,400)) #draw log text

    checker = 0
    for cust in customer:
        if cust.x <= cust.dest:
            if pause == False:
                cust.move()
            win.blit(walkRight[cust.getStep()//3], (cust.x,cust.y))
        else:
            if cust.getStatus() == 2:
                if pause == False:
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
check = 0
transactiondone=0

'''end temp variables'''



run = True

pause = False
while run:
    clock.tick(30)

    
    if len(customer)>0:
        if pygame.mouse.get_pos() >= (customer[len(customer)-1].x,customer[len(customer)-1].y) and pygame.mouse.get_pos() <= (customer[len(customer)-1].x+64,customer[len(customer)-1].y+64):
            print(customer[len(customer)-1].transaction.custid)
     
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_SPACE]:
        if pause == False:
            pause = True
        else:
            pause = False

    if pause == False:
        current_time = pygame.time.get_ticks()
        if current_time <100:
            start = current_time

        if current_time - start >1000:
            start = current_time
            """ Update time """
            start_time = addTime()
            timetext = font.render(timestr(),True,(0,0,0))
            

            for cust in customer:
                if cust.getStatus() == 1 and cust.getWait() == 1:
                    cust.status = 2
                    logtext = font.render(f"Customer ID {cust.transaction.custid} completed transaction",True,(0,0,0))

                    #Empty Text
                    itemtext[0] = font.render("",True,(0,0,0))
                    itemtext[1] = font.render("",True,(0,0,0))
                    itemtext[2] = font.render("",True,(0,0,0))
                    itemtext[3] = font.render("",True,(0,0,0))
                    itemtext[4] = font.render("",True,(0,0,0))

                    for j in range(len(cust.transaction.items)): # set item text
                        itemtext[j] = font.render(f"[{j+1}] {cust.transaction.items[j]['item']} ---  RM {cust.transaction.items[j]['price']} ",True,(0,0,0))

                elif cust.getStatus() == 1 and cust.getWait() == 0:
                    cust.wait = 1

        for i in range(transactiondone,len(transaction)):

            if timestr() == transaction[i].get_Arrival() and len(customer)<=transactiondone:
                customer.append(Cust(0,rows[2],320,transaction[i]))
                
                transactiondone = transactiondone + 1
        

    redrawGameWindow() 
    
    

pygame.quit()
