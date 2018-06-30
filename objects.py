#all the things is space
import math
BIG_G = 10

class gravobj():
    def __init__(self,x,y,mass):
        self.pos=[x,y]
        self.mass = mass
        self.gravP=[0,0]
        self.grav=[0,0]
        self.image = None
        self.size = [0,0]

    def assignImage(self, myimage, size):
        self.image = myimage
        self.size = size
    
    def setPos(self, pos):
        self.pos = pos
    def setGrav(self, grav):
        self.grav = grav

    def calulateGrav(self,gravObj):
        distance=((self.pos[0]- gravObj.pos[0])**2+(self.pos[1]- gravObj.pos[1])**2)**.5
        direction = self.calculateDirectionAngle(gravObj)
        if direction == [0,0]:
            return [0,0]
        totalmass = self.mass + gravObj.mass
        force = BIG_G*(totalmass/distance**2)/self.mass
        return([force*math.cos(direction),-force*math.sin(direction)])

    def calculateDirectionAngle(self,gravObj):
        try:
            direction=math.atan((self.pos[1] - gravObj.pos[1])/(self.pos[0] - gravObj.pos[0]))
            if self.pos[0] - gravObj.pos[0]>0:
                direction = direction-math.pi
                if direction<-math.pi:
                    direction=2*math.pi + direction
        except ZeroDivisionError:
            if self.pos[1]- gravObj.pos[1]>0:
                direction = -math.pi/2
            elif self.pos[1]- gravObj.pos[1]<0:
                direction = math.pi/2
            elif self.pos[1]- gravObj.pos[1]==0:
                return([0,0])
        
        return direction

    def adjustGrav(self,gravObjList):
        self.gravP = [0,0]
        for obj in gravObjList:
            Gvector = self.calulateGrav(obj)
            self.gravP[0] +=Gvector[0]
            self.gravP[1] +=Gvector[1]
    def getGravData(self):
        return self.gravP
    def getGravSpeedData(self):
        return self.grav
    def moveonG(self):
        self.changeVelocity()
        self.changePosition()
    def changeVelocity(self):
        self.grav[0]+=self.gravP[0]
        self.grav[1]+=self.gravP[1]
    def changePosition(self):
        self.pos[0]+=self.grav[0]
        self.pos[1]-=self.grav[1]