import pygame
import pygame.mixer
from tkinter import *
from tkinter import messagebox as mb


pygame.init()

Tk().wm_withdraw()
class Object(pygame.sprite.Sprite):
    def __init__(self,img,x,y,speed):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
RES=WIDTH,HEIGHT=800,600

# точка спавна игрока 
start1_x = 630
start1_y = 450
start2_x = 700
start2_y = 450




pygame.init()
pygame.mixer.music.load("02.mp3")
pygame.mixer.music.play()


screen=pygame.display.set_mode(RES)
pygame.display.set_caption("Doka 2")



#импорт изображений 
bg=pygame.transform.scale(pygame.image.load("images/фо.jpg"), (RES))
player1_img=pygame.transform.scale(pygame.image.load("images/player.png"), (50,50))
player2_img=pygame.transform.scale(pygame.image.load("images/io.png"), (50,50))
wall=pygame.transform.scale(pygame.image.load("images/wall.png"), (60,60))
enemy_img=pygame.transform.scale(pygame.image.load("images/Techies.png"), (59,59))
coin1_img=pygame.transform.scale(pygame.image.load("images/coin1.png"), (45,40))
coin2_img=pygame.transform.scale(pygame.image.load("images/coin2.png"), (45,60))
coin3_img=pygame.transform.scale(pygame.image.load("images/coin3.png"), (80,60))
# создание групп объектов
all_sprites = pygame.sprite.Group()
walls = pygame.sprite.Group()
enemies = pygame.sprite.Group()
items = pygame.sprite.Group()

#создание объектов 
player1 = Object(player1_img, start1_x, start1_y, 4)
all_sprites.add(player1)
player2 = Object(player2_img, start2_x, start2_y, 4)
all_sprites.add(player2)

#создание стен Оbjесt
wall1 = Object(wall, 0,0,0)
wall2 = Object(wall, 60,0,0)
wall3 = Object(wall, 0,60,0)
wall4 = Object(wall, 120,0,0)
wall5 = Object(wall, 0,120,0)
wall6 = Object(wall, 180,0,0)
wall7 = Object(wall, 0,180,0)
wall8 = Object(wall, 240,0,0)
wall9 = Object(wall, 0,240,0)
wall10 = Object(wall, 300,0,0)
wall11 = Object(wall, 0,300,0)
wall12 = Object(wall, 360,0,0)
wall13 = Object(wall, 0,360,0)
wall14 = Object(wall, 420,0,0)
wall15 = Object(wall, 0,420,0)
wall16 = Object(wall, 480,0,0)
wall17 = Object(wall, 0,480,0)
wall18 = Object(wall, 540,0,0)
wall19 = Object(wall, 600,0,0)
wall21 = Object(wall, 0,540,0) 
wall20 = Object(wall, 660,0,0)
wall22 = Object(wall, 720,0,0)
wall23 = Object(wall, 780,0,0)
wall24 = Object(wall, 780,60,0)
wall25 = Object(wall, 780,120,0)
wall26 = Object(wall, 780,180,0)
wall27 = Object(wall, 780,240,0)
wall28 = Object(wall, 780,300,0)
wall29 = Object(wall, 780,300,0)
wall30 = Object(wall, 780,360,0)
wall31 = Object(wall, 780,420,0)
wall32 = Object(wall, 780,480,0)
wall33 = Object(wall, 780,540,0)
wall34 = Object(wall, 60,540,0)
wall35 = Object(wall, 120,540,0)
wall36 = Object(wall, 180,540,0)
wall37 = Object(wall, 240,540,0)
wall38 = Object(wall, 300,540,0)
wall39 = Object(wall, 360,540,0)
wall40 = Object(wall, 420,540,0)
wall41 = Object(wall, 480,540,0)
wall42 = Object(wall, 540,540,0)
wall43 = Object(wall, 600,540,0)
wall44 = Object(wall, 660,540,0)
wall45 = Object(wall, 720,540,0)
wall46 = Object(wall, 720,360,0)
wall47 = Object(wall, 720,180,0)
wall48 = Object(wall, 540,360,0)
wall49 = Object(wall, 480,360,0)
wall50 = Object(wall, 480,300,0)
wall51 = Object(wall, 480,240,0)
wall52 = Object(wall, 480,180,0)
wall53 = Object(wall, 540,180,0)
wall54 = Object(wall, 480,120,0)
wall55 = Object(wall, 480,60,0)
wall56 = Object(wall, 420,360,0) 
wall57 = Object(wall, 300,360,0)
wall58 = Object(wall, 300,300,0)
wall59 = Object(wall, 300,240,0)
wall60 = Object(wall, 360,240,0)
wall61 = Object(wall, 420,240,0)
wall62 = Object(wall, 240,240,0)
wall63 = Object(wall, 60,240,0)
wall64 = Object(wall, 60,360,0)
wall65 = Object(wall, 240,360,0)






#враги
enemy1_x=200
enemy1_y=180
enemy1=Object(enemy_img,enemy1_x,enemy1_y,2)
enemy2_x=540
enemy2_y=250
enemy2=Object(enemy_img,enemy2_x,enemy2_y,2)
enemy3_x=60
enemy3_y=300
enemy3=Object(enemy_img,enemy3_x,enemy3_y,2)

#очки
coin1_x=440
coin1_y=310
coin1=Object(coin1_img,coin1_x,coin1_y,0)
coin2_x=250
coin2_y=100
coin2=Object(coin2_img,coin2_x,coin2_y,0)
coin3_x=600
coin3_y=100
coin3=Object(coin3_img,coin3_x,coin3_y,0)

coins_font = pygame.font.Font(None,35)
coins_text = coins_font.render("Монеты: 0", True , pygame.Color("white"))


walls.add(wall1,wall2,wall3,wall4,wall5,wall6,wall7,wall8,wall9,wall10,wall11,wall12,wall13,wall14,wall15,wall16,wall17,wall18,wall19,wall20,wall21,wall22,wall23,wall24,wall25,wall26,wall27,wall28,wall29,wall30,wall31,wall32,wall33,wall34,wall35,wall36,wall37,wall38,wall39,wall40,wall41,wall42,wall43,wall44,wall45,wall46,wall47,wall48,wall49,wall50,wall51,wall52,wall53,wall54,wall55,wall56,wall57,wall58,wall59,wall60,wall61,wall62,wall63,wall64,wall65 )
all_sprites.add(coin1,coin2,coin3,enemy1,enemy2,enemy3,wall1,wall2,wall3,wall4,wall5,wall6,wall7,wall8,wall9,wall10,wall11,wall12,wall13,wall14,wall15,wall16,wall17,wall18,wall19,wall20,wall21,wall22,wall23,wall24,wall25,wall26,wall27,wall28,wall29,wall30,wall31,wall32,wall33,wall34,wall35,wall36,wall37,wall38,wall39,wall40,wall41,wall42,wall43,wall44,wall45,wall46,wall47,wall48,wall49,wall50,wall51,wall52,wall53,wall54,wall55,wall56,wall57,wall58,wall59,wall60,wall61,wall62,wall63,wall64,wall65 )
enemies.add(enemy1,enemy2,enemy3)
items.add(coin1,coin2,coin3)

run = True
points=0
while run:
    if points == 3:
        mb.showinfo("Информация", "Вы выйграли ") 
        run = False 

    screen.blit(bg, (0,0))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()

    keys =pygame.key.get_pressed()
    if event.type == pygame.KEYDOWN:
        if keys[pygame.K_w]:
            player1.rect.y -= player1.speed
        if keys[pygame.K_s]:
            player1.rect.y += player1.speed
        if keys[pygame.K_d]:
            player1.image = pygame.transform.flip(player1_img, False, False)
            player1.rect.x += player1.speed
        if keys[pygame.K_a]:
            player1.image = pygame.transform.flip(player1_img, True, False)
            player1.rect.x -= player1.speed
        keys =pygame.key.get_pressed()


    if len(pygame.sprite.spritecollide(player2, walls, False)) > 0:
        player2.rect.x = start2_x
        player2.rect.y = start2_y
    if len(pygame.sprite.spritecollide(player1, walls, False)) > 0:
        player1.rect.x = start1_x
        player1.rect.y = start1_y

    if len(pygame.sprite.spritecollide(player2, enemies, False)) > 0:
        player2.rect.x = start2_x
        player2.rect.y = start2_y
    if len(pygame.sprite.spritecollide(player1, enemies, False)) > 0:
        player1.rect.x = start1_x
        player1.rect.y = start1_y        

    enemy1.rect.y += enemy1.speed
    if len(pygame.sprite.pygame.sprite.spritecollide(enemy1, walls, False)) > 0:
        enemy1.speed *= -1
    enemy2.rect.x += enemy2.speed
    if len(pygame.sprite.pygame.sprite.spritecollide(enemy2, walls, False)) > 0:
        enemy2.speed *= -1
    enemy3.rect.x += enemy3.speed
    if len(pygame.sprite.pygame.sprite.spritecollide(enemy3, walls, False)) > 0:
        enemy3.speed *= -1

    if len(pygame.sprite.pygame.sprite.spritecollide(player1, items, True)) > 0:
        points += 1
        coins_text = coins_font.render(("Монеты: " + str(points)), True , pygame.Color("white"))
        print(point)
    if len(pygame.sprite.pygame.sprite.spritecollide(player2, items, True)) > 0:
        points += 1
        coins_text = coins_font.render(("Монеты: " + str(points)), True , pygame.Color("white"))
        print(points)

    if event.type == pygame.KEYDOWN:
        if keys[pygame.K_UP]:
            player2.rect.y -= player2.speed
        if keys[pygame.K_DOWN]:
            player2.rect.y += player2.speed
        if keys[pygame.K_LEFT]:
            player2.image = pygame.transform.flip(player2_img, True, False)
            player2.rect.x -= player2.speed
        if keys[pygame.K_RIGHT]:
            player2.image = pygame.transform.flip(player2_img, False, False)
            player2.rect.x += player2.speed


        




    all_sprites.draw(screen)
    all_sprites.update()
    screen.blit(coins_text,(360,20))
    pygame.display.update()