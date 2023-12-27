#pong but extremely bad - have fun!! υa
from pygame import * #import pygame

background = (200, 255, 255) #background colour
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height)) 
window.fill(background)
#---------
class GameSprite(sprite.Sprite):
    def __init__ (self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65,65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image,(self.rect.x, self.rect.y))

class Player(GameSprite):
    def moveupdate(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 1:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < 620:
            self.rect.x += self.speed
    def fire(self):
        bullet = Bullet("bullet.png", self.rect.centerx, self.rect.top, -15)
        bullets.add(bullet)
#---------
clock = time.Clock()
FPS = 60
playing = True #game is running
#---------
while playing: #game loop
    for e in event.get():
        if e.type == QUIT:
            playing = False #game isnt running

    display.update()
    clock.tick(FPS)