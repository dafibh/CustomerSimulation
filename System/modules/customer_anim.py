class Customer_Anim:
    def __init__(self,x,y,dest,transaction):
        self.x = x
        self.y = y
        self.dest = dest
        self.step = 0
        self.status = 0
        self.wait = 0
        self.transaction = transaction

    def isCollide(self,mouseCoord):
        return (mouseCoord >= (self.x,self.y) and mouseCoord <= (self.x + 64, self.y + 64))

    def getStep(self):
        return self.step

    def getStatus(self):
        return self.status

    def wait(self):
        self.status = 1

    def done(self):
        self.status = 2

    def move(self):
        if self.x <=1000:
            self.x += 5
            self.step += 1
            if self.step + 1 >=27:
                self.step = 0

    def stop(self):
        self.step = 0

    def getWait(self):
        return self.wait