#pong but extremely bad have fun
from pygame import * #import pygame

background = (200, 255, 255) #background colour
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height)) 
window.fill(background)
font.init()
#---------
class GameSprite(sprite.Sprite):
    def __init__ (self, player_image, player_x, player_y, player_speed, width, height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (width,height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image,(self.rect.x, self.rect.y))

class Player(GameSprite):
    def moveupdateright(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 1:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 620:
            self.rect.y += self.speed
    def moveupdateleft(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 1:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 620:
            self.rect.y += self.speed

class Area():
    def __init__(self, x=0, y=0, width=10, height=10, color=(0,0,0)):
        self.rect = Rect(x, y, width, height)
        self.fill_color = color
class TextLabel(Area):
    def set_text(self,text,f_size,text_color):
        self.labelT = font.SysFont('trebuchet ms', f_size).render(text,True,text_color)
    def drawBl(self, sx=10, sy=10):
        window.blit(self.labelT,(self.rect.x+sx,self.rect.y+sy))
#---------
clock = time.Clock()
FPS = 60
playing = True #game is running
#---------
scorel = 0
scorer = 0
ball = GameSprite("ball (2).png", 250, 250, 3, 65,65)
paddlel = Player("player1paddle.png", 30, 200, 5, 50, 150)
paddler = Player("player2paddle.png", 510, 200, 5, 50, 150)
scoreleft = TextLabel(150,0, 50,50, (0,0,0))
scoreright = TextLabel(350,0, 50,50, (0,0,0))
finish = False
speedx = 4
speedy = 4
while playing: #game loop
    for e in event.get():
        if e.type == QUIT:
            playing = False #game isnt running
    if finish != True:
        window.fill(background)
        scoreright.set_text(str(scorer),46,(0,0,0))
        scoreleft.set_text(str(scorel),46,(0,0,0))
        ball.reset()
        ball.rect.x += speedx
        ball.rect.y += speedy
        paddlel.reset()
        paddler.reset()
        paddlel.moveupdateleft()
        paddler.moveupdateright()
        scoreright.drawBl()
        scoreleft.drawBl()
        if (sprite.collide_rect(paddlel, ball) and ball.rect.x < 100):
            speedx *= -1
        if sprite.collide_rect(paddler, ball) and ball.rect.x > 450:
            speedx *= -1
        if ball.rect.y > win_height-50 or ball.rect.y < 0:
            speedy *= -1
        
        if ball.rect.x >= 580:
            scorel += 1
            ball.rect.x = 250
        elif ball.rect.x <= 0:
            scorer += 1
            ball.rect.x = 250


    display.update()
    clock.tick(FPS)