from math import radians
import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()

pygame.mixer.music.set_volume(0.1)
background_music = pygame.mixer.music.load('BoxCat Games - CPU Talk.mp3')
pygame.mixer.music.play(-1)

music_bonus = pygame.mixer.Sound('smw_bonus_game_end.wav')

collision_noise = pygame.mixer.Sound('smw_coin.mp3')


pygame.display.set_caption('Test Game')

width = 640
height = 480

x = int(width/2)
y = int(height/2)

#fonte do contador
font = pygame.font.SysFont('arial', 40, True, True)

#valor inicial do contador
points = 0

x_blue = randint(40, 600)
y_blue = randint(50,430)

#controla a velocidade de frames por segundo(line:32)
clock = pygame.time.Clock()

screen = pygame.display.set_mode((width,height))

while True:
    clock.tick(30)
    screen.fill((0,0,0))
    msg = f"Pontos: {points}"
    text = font.render(msg, True, (255,255,255))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        '''
        if event.type == KEYDOWN:
            if event.key == K_a:
                x = x - 20
            if event.key == K_d:
                x = x + 20
            if event.key == K_w:
                y = y - 20
            if event.key == K_s:
                y = y + 20
                    '''
    #dando funçao para teclas(W,A,S,D)
    if pygame.key.get_pressed()[K_a]:
        x = x - 10  
    if pygame.key.get_pressed()[K_d]:
        x = x + 10
    if pygame.key.get_pressed()[K_w]:
        y = y - 10
    if pygame.key.get_pressed()[K_s]:
        y = y + 10
    
    #desenhando formas:
    #quadrado/retangulo
    ret_red = pygame.draw.rect(screen, (255,0,200), (x , y , 40 , 40))
    ret_blue = pygame.draw.rect(screen, (0,0,255), (x_blue , y_blue , 40 , 50))

    #criando colisao
    if ret_red.colliderect(ret_blue):
        x_blue = randint(40 , 600)
        y_blue = randint(50 , 430)
        points += 1
        collision_noise.play()
        if points == 50:
            music_bonus.play()   
    #escrevendo o contador de pontos
    screen.blit(text, (420,40))
    pygame.display.update()