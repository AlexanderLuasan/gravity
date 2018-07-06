#The camera class

class cammera():
    def __init__(self,x,y):
        self.x=-400+x
        self.y=-400+y
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
    def center_on(self, obj):
        "centers the cammera on the gravobj in the argument"
        (self.x, self.y) = (obj.pos[0] - 500, obj.pos[1] - 500)