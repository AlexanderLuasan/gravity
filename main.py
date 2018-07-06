#main function
import pygame
import math
import world
import visual
pygame.init()


clock = pygame.time.Clock()
gravList = world.getGravList()
#cam

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
                    visual.camra.adjPos([0,15])
                elif event.key == 274: #down
                    visual.camra.adjPos([0,-15])
                elif event.key == 276: #left
                    visual.camra.adjPos([15,0])
                elif event.key == 275: #right
                    visual.camra.adjPos([-15,0])
                elif event.key == 119: #w,a,s,d = 119, 97, 115, 100
                    world.player_charecter.engines_on[0] += 1
                elif event.key == 115:
                    world.player_charecter.engines_on[0] -= 1
                elif event.key == 97:
                    world.player_charecter.engines_on[1] += 1
                elif event.key == 100:
                    world.player_charecter.engines_on[1] -= 1
                elif event.key == 32:
                    #print(visual.camra.getx, visual.camra.gety) this doesn't work, for some reason.
                    #Needed to resort to:
                    print((visual.camra.x, visual.camra.y))
                    print(world.player_charecter.pos)
                    visual.camra.center_on(world.player_charecter)
                else:
                    print(event.key)

            elif event.type == pygame.KEYUP:
                if event.key == 0:
                    pass
                elif event.key == 119: #w,a,s,d = 119, 97, 115, 100
                    world.player_charecter.engines_on[0] -= 1
                elif event.key == 115:
                    world.player_charecter.engines_on[0] += 1
                elif event.key == 97:
                    world.player_charecter.engines_on[1] -= 1
                elif event.key == 100:
                    world.player_charecter.engines_on[1] += 1
                else:
                    pass
                    #print(event.key)
    world.updateList()
    visual.drawStart()
    visual.drawList(gravList)
    visual.drawEnd()
    pygame.display.flip()
    for first in gravList:
        for second in gravList:
            if first!=second:
                try:
                    #print(first.colision(second))
                    pass
                except:
                    pass
    
    clock.tick(30)
pygame.quit()
