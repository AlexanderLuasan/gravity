#main function
import pygame
import math
import world
import visual
pygame.init()


clock = pygame.time.Clock()
center = world.objects.gravobj(200,200,300)
player = world.objects.gravobj(500,500,400)
third = world.objects.gravobj(200,500,800)
gravList = [center,player,third]
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
    for i in gravList:
        i.adjustGrav(gravList)
    for i in gravList:
        i.moveonG()
    
    visual.drawStart()
    visual.drawList(gravList)
    visual.drawEnd()
    pygame.display.flip()
    clock.tick(30)
pygame.quit()
