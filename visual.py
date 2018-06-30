#where we draw stuff
import camera
import pygame
pygame.init()

camra = camera.cammera()
screen = pygame.display.set_mode([800,800])
pygame.display.set_caption("gravtest")


def drawStart():
    screen.fill((0,0,0))
    
def drawList(gravList):
    for i in gravList:
        image = pygame.Surface([40,40])
        image.fill((255,255,255))
        screen.blit(image,pygame.Rect(i.pos[0]-20+camra.getx(),i.pos[1]-20+camra.gety(),40,40))
        end = i.getGravSpeedData()
        pygame.draw.line(screen,(255,0,0),[i.pos[0]+camra.getx(),i.pos[1]+camra.gety()],[i.pos[0]+100*end[0]+camra.getx(),i.pos[1]-100*end[1]+camra.gety()],2)
        try:
            end = i.forward_axis_to_cords()
            pygame.draw.line(screen,(0,255,0),[i.pos[0]+camra.getx(),i.pos[1]+camra.gety()],[i.pos[0]+50*end[0]+camra.getx(),i.pos[1]-50*end[1]+camra.gety()],2)
        except:
            pass

def drawEnd():
    pygame.display.flip()