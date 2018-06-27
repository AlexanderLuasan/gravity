import pygame
import math
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode([800,800])
pygame.display.set_caption("gravtest")
BIG_G = 10
class cammera():
    def __init__(self):
        self.x=-400
        self.y=-400
        self.zoom = 1
    def adjPos(self,pos):
        self.x+=pos[0]
        self.y+=pos[1]
    def setZoom(self,z):
        self.zoom=z
    def getx(self):
        return self.x
    def gety(self):
        return self.y
class gravobj():
    def __init__(self,x,y,mass):
        self.x=x
        self.y=y
        self.pos=[x,y]
        self.mass = mass
        self.gravP=[0,0]
        self.grav=[0,0]
    def calulateGrav(self,gravObj):
        distance=((self.pos[0]- gravObj.pos[0])**2+(self.pos[1]- gravObj.pos[1])**2)**.5
        
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
        totalmass=self.mass + gravObj.mass
        #printout
        '''
        print("distance is ",distance)
        if direction != None:
            print("direction is ",direction)
            print("pos is" , gravObj.pos,"deg",direction*180.0/math.pi)
        else:
            print("direction is none")
        print("totalmass is ",totalmass)
        '''
        force = BIG_G*(totalmass/distance**2)/self.mass
        return([force*math.cos(direction),-force*math.sin(direction)])
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
        self.grav[0]+=self.gravP[0]
        self.grav[1]+=self.gravP[1]
        self.pos[0]+=self.grav[0]
        self.pos[1]-=self.grav[1]
            

        
#the things
center = gravobj(200,200,300)
player = gravobj(500,500,400)
third = gravobj(200,500,800)
gravList = [center,player,third]
#cam
camra = cammera()
#test cases
'''
player.pos[1]=40
for i in [0,10,20,30,40]:
    player.pos[0]=i
    center.calulateGrav(player)
for i in [30,20,10,0,-10,-20,-30,-40]:
    player.pos[1]=i
    center.calulateGrav(player)
for i in [30,20,10,0,-10,-20,-30,-40]:
    player.pos[0]=i
    center.calulateGrav(player)
for i in [-30,-20,-10,0,10,20,30,40]:
    player.pos[1]=i
    center.calulateGrav(player) 
for i in [-30,-20,-10,0]:
    player.pos[0]=i
    center.calulateGrav(player)     
'''

done=False
while (True != done):
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                fullexit = True
            elif event.type==pygame.KEYDOWN:
                if event.key == 273: #up
                    camra.adjPos([0,10])
                elif event.key == 274: #down
                    camra.adjPos([0,-10])
                elif event.key == 276: #left
                    camra.adjPos([-10,0])
                elif event.key == 275: #right
                    camra.adjPos([10,0])
                elif event.key == 32:
                    print()
                else:
                    print(event.key)
                
            elif event.type == pygame.KEYUP:
                if event.key == 0:
                    pass
                else:
                    pass
                    #print(event.key)
    screen.fill((0,0,0))
    for i in gravList:
        i.adjustGrav(gravList)
    for i in gravList:
        i.moveonG()
    for i in gravList:
        image = pygame.Surface([40,40])
        image.fill((255,255,255))
        screen.blit(image,pygame.Rect(i.pos[0]-20+camra.getx(),i.pos[1]-20+camra.gety(),40,40))
        end = i.getGravSpeedData()
        pygame.draw.line(screen,(255,0,0),[i.pos[0]+camra.getx(),i.pos[1]+camra.gety()],[i.pos[0]+100*end[0]+camra.getx(),i.pos[1]-100*end[1]+camra.gety()],2)
    pygame.display.flip()
    clock.tick(30)
pygame.quit()
