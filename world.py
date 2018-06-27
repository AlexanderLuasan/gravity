#simulation
import objects
import player 
import checkpoints

#
#setup
center = objects.gravobj(200,200,300)
player = objects.gravobj(500,500,400)
third = objects.gravobj(200,500,800)
gravList = [center,player,third]

def getGravList():
    return gravList
def updateList():
    for i in gravList:
        i.adjustGrav(gravList)
    for i in gravList:
        i.moveonG()    