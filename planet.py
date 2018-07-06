import objects
class simpleSpaceObj(objects.gravobj): #has features of colision needed for most space objects using a radius 
    def __init__(self,x,y,mass,radius=50,color=(255,255,0)):
        super().__init__(x,y,mass)
        self.radius = radius
        self.color = color
    def colision(self,other): #returns true if they overlap
        try:
            threshHold = self.radius + other.radius
        except:
            return(None)
        distance=((self.pos[0]-other.pos[0])**2 + (self.pos[1]-other.pos[1])**2)**.5
        
        if distance<=threshHold:
            return True
        else:
            return False
    def test(self):
        print("i am simple planet")