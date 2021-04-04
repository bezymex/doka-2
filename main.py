import pygame
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
start_x = 630
start_y = 450
start1_x = 700
start1_y = 450




pygame.init()
pygame.mixer.music.load("02.mp3")
pygame.mixer.music.play()


screen=pygame.display.set_mode(RES)
pygame.display.set_caption("Doka 2")



#импорт изображений 
bg=pygame.transform.scale(pygame.image.load("images/фо.jpg"), (RES))
player_img=pygame.transform.scale(pygame.image.load("images/player.png"), (50,50))
player1_img=pygame.transform.scale(pygame.image.load("images/io.png"), (50,50))
wall=pygame.transform.scale(pygame.image.load("images/wall.png"), (60,60))
enemy_img=pygame.transform.scale(pygame.image.load("images/Techies.png"), (100,100))


# создание групп объектов
all_sprites = pygame.sprite.Group()
walls = pygame.sprite.Group()
enemies = pygame.sprite.Group()


#создание объектов 
player = Object(player_img, start_x, start_y, 4)
all_sprites.add(player)
player1 = Object(player1_img, start1_x, start1_y, 4)
all_sprites.add(player1)

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


enemy1_x=430
enemy1_y=250
enemy1=Object(enemy_img,enemy1_x,enemy1_y,2)
enemy2_x=500
enemy2_y=300
enemy2=Object(enemy_img,enemy2_x,enemy2_y,2)
enemy3_x=250
enemy3_y=230
enemy3=Object(enemy_img,enemy3_x,enemy3_y,2)



walls.add(wall1,wall2,wall3,wall4,wall5,wall6,wall7,wall8,wall9,wall10,wall11,wall12,wall13,wall14,wall15,wall16,wall17,wall18,wall19,wall20,wall21,wall22,wall23,wall24,wall25,wall26,wall27,wall28,wall29,wall30,wall31,wall32,wall33,wall34,wall35,wall36,wall37,wall38,wall39,wall40,wall41,wall42,wall43,wall44,wall45)
all_sprites.add(enemy1,enemy2,enemy3,wall1,wall2,wall3,wall4,wall5,wall6,wall7,wall8,wall9,wall10,wall11,wall12,wall13,wall14,wall15,wall16,wall17,wall18,wall19,wall20,wall21,wall22,wall23,wall24,wall25,wall26,wall27,wall28,wall29,wall30,wall31,wall32,wall33,wall34,wall35,wall36,wall37,wall38,wall39,wall40,wall41,wall42,wall43,wall44,wall45)
enemies.add(enemy1,enemy2,enemy3)

run = True
while run:
    screen.blit(bg, (0,0))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()

    keys =pygame.key.get_pressed()
    if event.type == pygame.KEYDOWN:
        if keys[pygame.K_w]:
            player.rect.y -= player.speed
        if keys[pygame.K_s]:
            player.rect.y += player.speed
        if keys[pygame.K_d]:
            player.image = pygame.transform.flip(player_img, False, False)
            player.rect.x += player.speed
        if keys[pygame.K_a]:
            player.image = pygame.transform.flip(player_img, True, False)
            player.rect.x -= player.speed
        keys =pygame.key.get_pressed()


    if len(pygame.sprite.spritecollide(player1, walls,enemies, False)) > 0:
        player1.rect.x = start1_x
        player1.rect.y = start1_y
    if len(pygame.sprite.spritecollide(player, walls,enemies, False)) > 0:
        player.rect.x = start_x
        player.rect.y = start_y

    enemy1.rect.y += enemy1.speed
    if len(pygame.sprite.pygame.sprite.spritecollide(enemy1, walls, False)) > 0:
        enemy1.speed *= -2
    enemy2.rect.x -= enemy2.speed
    if len(pygame.sprite.pygame.sprite.spritecollide(enemy2, walls, False)) > 0:
        enemy2.speed *= -2
    enemy3.rect.x += enemy3.speed
    if len(pygame.sprite.pygame.sprite.spritecollide(enemy3, walls, False)) > 0:
        enemy2.speed *= -2

    if event.type == pygame.KEYDOWN:
        if keys[pygame.K_UP]:
            player1.rect.y -= player1.speed
        if keys[pygame.K_DOWN]:
            player1.rect.y += player1.speed
        if keys[pygame.K_LEFT]:
            player1.image = pygame.transform.flip(player1_img, True, False)
            player1.rect.x -= player1.speed
        if keys[pygame.K_RIGHT]:
            player1.image = pygame.transform.flip(player1_img, False, False)
            player1.rect.x += player1.speed


        




    all_sprites.draw(screen)
    all_sprites.update()
    pygame.display.update()