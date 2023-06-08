from pygame import *
from random import randint
class GameSprite(sprite.Sprite):
    def __init__(self,player_image,player_x,player_y,player_width,player_hight , player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(player_width,player_hight))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite): 
    def update(self): 
        keys_pressed = key.get_pressed() 
        if keys_pressed[K_DOWN] and self.rect.y < 395: 
            self.rect.y +=self.speed 
        if keys_pressed[K_UP] and self.rect.y>0: 
            self.rect.y -= self.speed
    def update2(self): 
        keys_pressed = key.get_pressed() 
        if keys_pressed[K_s] and self.rect.y < 395: 
            self.rect.y +=self.speed 
        if keys_pressed[K_w] and self.rect.y>0: 
            self.rect.y -= self.speed

 


window = display.set_mode((700, 500))
display.set_caption('Шутер')
background = transform.scale(image.load('galaxy.jpg'),(700,500))
mixer.init()
mixer.music.load('space.ogg')
mixer.music.play()

player = Player('png-clipart-bar-persegi-image-file-formats-rectangle-thumbnail.png',545,50,20, 220, 3)
player2 = Player('png-clipart-bar-persegi-image-file-formats-rectangle-thumbnail.png',50,50,20, 220, 3)




finish = False

lost = 0
count = 0
font.init()
font = font.Font(None, 36)
text_lose = font.render('player1 LOSE', True, (255,255,255))

text_count = font.render('player2 LOSE', True, (255,255,255))






game = True
clock = time.Clock()
ball = GameSprite('football_PNG1080.png', 320,220,50,50,0)

ball_y= 3
ball_x= 3

while game: 

    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.blit(background, (0, 0))
        player.reset() 
        player.update() 
        player2.reset() 
        player2.update2()
        ball.rect.y += ball_y
        ball.rect.x += ball_x
        if ball.rect.y >450 or ball.rect.y <0:
            ball_y=-1
        if sprite.collide_rect(ball, player) or sprite.collide_rect(ball, player2):
            ball_x =-1
        ball.reset()
        
        if ball.rect.x <-10:
            finish = True
            window.blit(text_lose,(200,200))
        if ball.rect.x >710:
            finish = True
            window.blit(text_count,(200,200))
    else:
        finish = False

        time.delay(3000)
    display.update()

    time.delay(10)

