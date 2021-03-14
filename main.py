import pygame
class Object(pygame.sprite.Sprite):
    def __init__(self,img,x,y,speed):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
RES=WIDTH,HEIGHT=1280,720
FPS=60
pygame.init()
pygame.mixer.music.load("02.mp3")
pygame.mixer.music.play(-1,10)

screen=pygame.display.set_mode(RES)
pygame.display.set_caption("Doka 2")
clock=pygame.time.Clock()
pygame.display.flip()
clock.tick(FPS)

run = True 
bg=pygame.transform.scale(pygame.image.load("images/01.jpg"), (RES))

while run:
    screen.blit(bg, (0,0))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:


            exit()
        pygame.display.flip()
        clock.tick(FPS)







    pygame.display.update()