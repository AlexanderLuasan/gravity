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

#print(isinstance(objects.gravobj(1,1,1), int))

class playerCharecter(objects.gravobj):
    def __init__(self,x,y,mass):
        super().__init__(x,y,mass)
        self.hull_health = 1
        self.shield = 0
        self.rotational_speed = 0 #im going to measure this in radians per 10 frames. Positive value = counter clockwise, negative value = clockwise
        self.forward_axis = objects.math.pi / 2 #this is what "forward" is relative to the player's ship measured in radians
        self.turnspeed = .1
        self.forwardspeed = .1 #these last two can be upgraded by purchases later
    
    def forward_axis_to_cords(self):
        return [objects.math.cos(self.forward_axis),objects.math.sin(self.forward_axis)]

    def fireForwardEngine(self):
        self.grav[0] += objects.math.cos(self.forward_axis)
        self.grav[1] += objects.math.sin(self.forward_axis)
    
    def fireReverseEngine(self):
        self.grav[0] -= objects.math.cos(self.forward_axis)
        self.grav[1] -= objects.math.sin(self.forward_axis)
    
    def fireLeftTuringinEngine(self):
        self.rotational_speed += self.turnspeed

    def fireRightTurningEngine(self):
        self.rotational_speed -= self.turnspeed
    
    def moveonG(self):
        super().moveonG()
        self.forward_axis += self.rotational_speed/10

if __name__ == "__main__":
    me = playerCharecter(1,1,1)

#wasd = 119, 97, 115, 100

    

#you know what might be fun? super limited fuel, you have a line that shows your tradjectory
#can conserve fuel by flinging yourself with physics
#maybe you can place tempory mass objects? like, create a gravton field for x energy 
#that acts like a planet of y mass, so you can do the aforementioned physics flinging?
#maybe you can create proximity mines that are affected by physics? so you can fling them at aliens?