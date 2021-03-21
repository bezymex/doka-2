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
start_x = 100
start_y = 120
start1_x = 200
start1_y = 200




pygame.init()
pygame.mixer.music.load("02.mp3")
pygame.mixer.music.play()


screen=pygame.display.set_mode(RES)
pygame.display.set_caption("Doka 2")



#импорт изображений 
bg=pygame.transform.scale(pygame.image.load("images/фо.jpg"), (RES))
player_img=pygame.transform.scale(pygame.image.load("images/player.png"), (64,64))
player1_img=pygame.transform.scale(pygame.image.load("images/pudge.png"), (64,64))


# создание групп объектов
all_sprites = pygame.sprite.Group()


#создание объектов 
player = Object(player_img, start_x, start_y, 4)
all_sprites.add(player)
player1 = Object(player1_img, start1_x, start1_y, 4)
all_sprites.add(player1)

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