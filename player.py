#the player class
import objects
"""
Player:
	resourse:
		hull/armmor/health count of physical damage
		sheild made from energy temporary recharges heat/energey
		energy spend for light life support
		fuel with energey is spend for movment
		food ticks down over time

	spend:
		map cost energey
		sonnar on/off
		fire engins fuel
		hit objects hull
		though suns corona and planets anmoherer sheild
		recahrge sheild with energy
		


	movment stats:

		rotation speed in degress perframe or maybe per 10 or 60 frames
		4 enges on in each directions with an arry of burn levels/percents
			rear 10 or 5 left 3 right 3 front 5
			note mass should be taken into acount

"""

class playerCharecter(objects.gravobj):
    def __init__(self,x,y,mass, initial_hull):
        super.__init__()
        self.hull_health = 1
        self.shield = 0
        self.rotational_speed = 0 #im going to measure this in radians per 10 frames. Positive value = clockwise, negative value =  counter clockwise
        self.forward = objects.math.pi / 2 #this is what "forward" is relative to the player's ship.
    
    def fireEngines(self):
        self.
    
    def moveonG(self):
        super.moveonG()
        self.forward = 



    

    



#how do i deal with engines
    
#wasd = 119, 97, 115, 100

    

