import pygame
import random
import math
from colorsys import hsv_to_rgb

pygame.init()
font = pygame.font.Font('freesansbold.ttf', 40)
font1 = pygame.font.Font('freesansbold.ttf', 150)
fps = 30
clock = pygame.time.Clock()


screen_width = 25*52
screen_height = 14*52 + 100
screen = pygame.display.set_mode((screen_width, screen_height))

mountain1 = pygame.image.load('mountain_brown.svg').convert_alpha()
mountain2 = pygame.image.load('mountain_green.svg').convert_alpha()
tree1 = pygame.image.load('tree1.svg').convert_alpha()
tree2 = pygame.image.load('tree2.svg').convert_alpha()
volcano = pygame.image.load('volcano.svg').convert_alpha()
splash_screen = pygame.image.load('splash.png').convert()
win = pygame.image.load('win.png').convert()
dig = pygame.image.load('dig.svg')

bg_color = (247, 230, 166)
interface_color = (168, 222, 126)
dark_green = (68, 99, 43)
dark_red = (82, 24, 24)
white = (255,255,255)
red = (235, 87, 87)

hue = 0

click = 0
treasure_x = random.randint(0, screen_width)
treasure_y = random.randint(0, screen_height-100)
dist = 996
x = 0
y = 0
max_dist = math.sqrt(screen_width**2 + (screen_height-100)**2)
splash = True
score = True
run = True

############[ MAP ]############
rows, columns = 25, 14
array = [[random.randint(0,30) for i in range(rows)] for j in range(columns)]

############[ CLICK MAP ]############
click_array = [[0 for i in range(rows)] for j in range(columns)]


############[ SPLASH ]############

while splash:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            splash = False
            run = False
            score = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            splash = False

    if hue >= 1:
        hue = 0
    else:
        hue += 0.01

    dyn_color = hsv_to_rgb(hue,0.6,180)

    screen.blit(splash_screen, (0,0))
    text = font1.render('Treasure hunt', True, dyn_color)
    screen.blit(text, (150,150))



    pygame.display.update()
    clock.tick(fps)


############[ GAME ]############
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            score = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            click += 10
            x,y = pygame.mouse.get_pos()
            click_array[int(y/52)][int(x/52)] = 1




    screen.fill(bg_color)
    for j in range(0, screen_height - 100, 52):
        for i in range(0,screen_width, 52):
            rectangle = pygame.Rect(i, j, 50, 50)
            if i < pygame.mouse.get_pos()[0] < i+52 and j < pygame.mouse.get_pos()[1] < j+52:
                color = (222, 202, 131)
            else:
                color = (242, 223, 153)
            pygame.draw.rect(screen, color, rectangle)

            if not(click_array[int(j/52)][int(i/52)]):
                if array[int(j/52)][int(i/52)] == 1:
                    screen.blit(mountain1, (i,j))
                elif array[int(j/52)][int(i/52)] == 2:
                    screen.blit(mountain2, (i,j))
                elif array[int(j/52)][int(i/52)] == 3:
                    screen.blit(tree1, (i,j))
                elif array[int(j/52)][int(i/52)] == 4:
                    screen.blit(tree2, (i,j))
                elif array[int(j/52)][int(i/52)] == 5:
                    screen.blit(volcano, (i,j))
                else:
                    continue
            else:
                screen.blit(dig, (i,j))


    rectangle = pygame.Rect(0, 728, screen_width, 100)
    pygame.draw.rect(screen, interface_color, rectangle)
    rectangle = pygame.Rect(20, 750, screen_width-300, 50)
    pygame.draw.rect(screen, white, rectangle)
    rectangle = pygame.Rect(screen_width-200, 750, 150, 50)
    pygame.draw.rect(screen, white, rectangle)

    actual_dist = math.sqrt((treasure_x - x)**2 + (treasure_y - y)**2)
    if actual_dist < 70:
        run = False
    prox = 996*(1-actual_dist/max_dist)
    proximity = pygame.Rect(22,752, prox, 46)
    pygame.draw.rect(screen, red, proximity)
    text = font.render('Proximity', True, dark_red)
    screen.blit(text, (450,755))
    text = font.render('$', True, dark_green)
    screen.blit(text, (screen_width-190,755))
    text = font.render(str(click), True, dark_green)
    screen.blit(text, (screen_width-160,755))


    pygame.display.update()
    clock.tick(fps)

############[ SCORE ]############
while score:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            score = False

        screen.blit(win, (0,0))
        text = font.render('$'+str(click), True, dark_green)
        screen.blit(text, (820,350))
        pygame.display.update()
        clock.tick(fps)




