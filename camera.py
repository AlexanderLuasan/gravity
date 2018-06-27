#The camera class

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