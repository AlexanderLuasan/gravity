#where we draw stuff
import camera
import pygame
pygame.init()

camra = camera.cammera(400,400)
screen = pygame.display.set_mode([800,800])
pygame.display.set_caption("gravtest")


def drawStart():
    screen.fill((0,0,0))
    
def drawList(gravList):
    for i in gravList:
        bitmap = None
        try:
            if i.image != None:
                bitmap = i.image
            else:
                temp =i.ggg
                
        except:

            try: 
                if i.radius > 0 and i.color != None:
                    bitmap = pygame.Surface([i.radius*2,i.radius*2])
                    bitmap.fill((0,0,1))
                    bitmap.set_colorkey((0,0,1))
                    pygame.draw.circle(bitmap, i.color, [i.radius,i.radius], i.radius)
            except:
                bitmap = pygame.Surface([40,40])
                bitmap.fill((255,255,255))

        screen.blit(bitmap,pygame.Rect(i.pos[0]-bitmap.get_width()/2+camra.getx(),i.pos[1]-bitmap.get_height()/2+camra.gety(),40,40))
        
        #out data
        end = i.getGravSpeedData()
        pygame.draw.line(screen,(255,0,0),[i.pos[0]+camra.getx(),i.pos[1]+camra.gety()],[i.pos[0]+100*end[0]+camra.getx(),i.pos[1]-100*end[1]+camra.gety()],2)
        try:
            end = i.forward_axis_to_cords()
            pygame.draw.line(screen,(0,255,0),[i.pos[0]+camra.getx(),i.pos[1]+camra.gety()],[i.pos[0]+50*end[0]+camra.getx(),i.pos[1]-50*end[1]+camra.gety()],2)
        except:
            pass

def drawEnd():
    pygame.display.flip()