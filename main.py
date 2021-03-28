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
start_y = 500
start1_x = 700
start1_y = 500




pygame.init()
pygame.mixer.music.load("02.mp3")
pygame.mixer.music.play()


screen=pygame.display.set_mode(RES)
pygame.display.set_caption("Doka 2")



#импорт изображений 
bg=pygame.transform.scale(pygame.image.load("images/фо.jpg"), (RES))
player_img=pygame.transform.scale(pygame.image.load("images/player.png"), (64,64))
player1_img=pygame.transform.scale(pygame.image.load("images/io.png"), (80,80))
wall=pygame.transform.scale(pygame.image.load("images/wall.png"), (80,80))


# создание групп объектов
all_sprites = pygame.sprite.Group()
walls = pygame.sprite.Group()


#создание объектов 
player = Object(player_img, start_x, start_y, 4)
all_sprites.add(player)
player1 = Object(player1_img, start1_x, start1_y, 4)
all_sprites.add(player1)

#создание стен Оbjесt
wall1 = Object(wall, 500,500,0)
wall2 = Object(wall, 270,420,0)
wall3 = Object(wall, 710,345,0)
wall4 = Object(wall, 620,330,0)
wall5 = Object(wall, 510,360,0)
wall6 = Object(wall, 350,405,0)
wall7 = Object(wall, 170,405,0)
wall8 = Object(wall, 80,405,0)
wall9 = Object(wall, 170,320,0)
wall10 = Object(wall, 390,210,0)
wall11 = Object(wall, 410,140,0)
wall12 = Object(wall, 396,70,0)
wall13 = Object(wall, 405,10,0)
wall14 = Object(wall, 560,150,0)
wall15 = Object(wall, 490,140,0)
wall16 = Object(wall, 170,250,0)

walls.add(wall1,wall2,wall3,wall4,wall5,wall6,wall7,wall8,wall9,wall10,wall11,wall12,wall13,wall14,wall15,wall16)
all_sprites.add(wall1,wall2,wall3,wall4,wall5,wall6,wall7,wall8,wall9,wall10,wall11,wall12,wall13,wall14,wall15,wall16)

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