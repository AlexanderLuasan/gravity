#simulation
import player 
import checkpoints
import planet

#
#setup
center = planet.simpleSpaceObj(200,200,300)

player_charecter = player.playerCharecter(500,500,400)
third = planet.simpleSpaceObj(200,500,800)
gravList = [center,player_charecter,third]

def getGravList():
    return gravList
def updateList():
    for i in gravList:
        i.adjustGrav(gravList)
    for i in gravList:
        i.moveonG()


