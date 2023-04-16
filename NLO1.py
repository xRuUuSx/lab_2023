import random

import pygame
from pygame.draw import *
import sys

pygame.init()

H = 800
W = 800

FPS = 30
screen = pygame.display.set_mode((W, H))

# colors
black = [0, 0, 0]
white = [255, 255, 255]
mon_colors = [250, 250, 250]
gray = [145, 145, 145]
colors_metal = [172, 172, 172]
colors_glass =[175, 218, 252]
white_gray = [230, 220, 210]
black_gray = [90, 90, 90]
black_green = [0, 100, 90]
black_blue = [0, 60, 80]
red = [255, 0, 0]

# background
background = pygame.Surface((W, H))
rect(background, black_green, [0, W / 2, W, H])
rect(background, black_blue, [0, - W / 2, W, W])

'''sky'''
# sky = pygame.Surface((W, H / 2))
# sky.set_alpha(100)
'''cloud gray'''
cloud_gray = pygame.Surface((W / 2, H / 8))
cloud_gray.set_colorkey(black)
ellipse(cloud_gray, black_gray, (0, 0, W / 3, H / 8))

'''cloud white gray'''
cloud_white_gray = pygame.Surface((W / 2, H / 8))
cloud_white_gray.set_colorkey(black)
ellipse(cloud_white_gray, white_gray, (0, 0, W / 3, H / 9))
'''mon'''
mon = pygame.Surface((W / 4, H / 4))
mon.set_colorkey(black)
circle(mon, mon_colors, (W / 8, H / 8), 100)


beam_flying_saucers = pygame.Surface((W / 4, H / 4))
beam_flying_saucers.set_colorkey(black)

polygon(beam_flying_saucers, white, [[0, W / 4], [100, H/11], [W / 4, H / 4 ]])
beam_flying_saucers.set_alpha(25)





'''  flying saucers '''

main_fling_saucers = pygame.Surface((W / 4, H / 4))
main_fling_saucers.set_colorkey(black)
main_fling_saucers.set_alpha(50)

'''flying saucers'''
flying_saucers = pygame.Surface((W / 4, H / 4))
flying_saucers.blit(beam_flying_saucers, (0, 0))
flying_saucers.set_colorkey(black)
ellipse(flying_saucers, colors_metal, (0, H / 4 / 10, W / 4, H / 10))
ellipse(flying_saucers, colors_glass, (W / 4 / 6, 0, W / 6, H / 12))
circle(flying_saucers, colors_glass, ((W / 8), (H / 9.5)), 13)
circle(flying_saucers, colors_glass, ((W / 16), (H / 10.5)), 13)
circle(flying_saucers, colors_glass, (W / 4 / 10, H / 4 / 3.5), 13)
circle(flying_saucers, colors_glass, ((W / 5.5), (H / 10.5)), 13)
circle(flying_saucers, colors_glass, ((W / 4.5), (H / 4 / 3.5)), 13)

''' beam flying saucers'''
# beam_flying_saucers = pygame.Surface((W / 4, H / 4))
# beam_flying_saucers.set_colorkey(black)
#
# polygon(beam_flying_saucers, white, [[0, W / 4], [100, H/11], [W / 4, H / 4 ]])
# beam_flying_saucers.set_alpha(25)



# main_fling_saucers.blit(beam_flying_saucers, (0, 0))
# main_fling_saucers.blit(flying_saucers, (0, 0))






# beam_flying_saucers.blit(flying_saucers, (0, 0))
background.blit(mon, (W - W / 3, H / 10))
background.blit(cloud_gray, (W - W / 3, H / 10))
background.blit(cloud_gray, (0, 0))
background.blit(cloud_white_gray, (100, 100))
background.blit(flying_saucers, (W / 4.6, H / 2.8))

screen.blit(background, (0, 0))

# def background():
#
# # back_ground = pygame.Surface ((800, 800))
#     rect(back_ground, black_green, [0, 400, 800, 800])
#     rect(back_ground, black_blue, [0, -400, 800, 800])
#
#
# sky = pygame.Surface((400, 400))
# circle(sky, white, (600, 200), 100)
# ellipse(sky, black_gray, (-300, 0, 800, 120))
# ellipse(sky, gray, (-50, 200, 450, 120))
# ellipse(sky, gray, (-50, 50, 150, 200))
# ellipse(sky, gray, (500, 0, 450, 120))
# ellipse(sky, gray, (550, 200, 550, 120))
# ellipse(sky, black_gray, (-100, 150, 650, 120))
# ellipse(sky, gray, (180, 100, 350, 120))
#
#
#
#
# def alion():
#     pass
#
#
# flying_saucers = pygame.Surface((50))
#     polygon(screen, white,
#             [[300, 350], [200, 500], [400, 500]])
#
#
#
#     ellipse(screen, colors_metal, (100, 250, 400, 140))
#     ellipse(screen, black, (100, 250, 400, 140), 2)
#     ellipse(screen, white_gray, (150, 240, 300, 100))
#     ellipse(screen, black, (150, 240, 300, 100), 2)
#
#     circle(screen, white, (140, 320), 17)
#     circle(screen, white, (200, 350), 17)
#     circle(screen, white, (270, 365), 17)
#     circle(screen, white, (340, 365), 17)
#     circle(screen, white, (400, 350), 17)
#     circle(screen, white, (460, 320), 17)


pygame.display.update()

clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()

