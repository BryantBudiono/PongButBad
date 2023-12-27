#pong but extremely bad - have fun!! υa
from pygame import * #import pygame

background = (200, 255, 255) #background colour
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height)) 
window.fill(background)
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