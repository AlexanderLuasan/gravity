#main function
import pygame
import math


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
