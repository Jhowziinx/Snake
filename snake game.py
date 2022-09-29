
from math import radians
from operator import truediv
import pygame
from pygame.locals import *
from sys import exit
from random import randint
from time import sleep

pygame.init() #inicando a biblioteca

#Musica de fundo
pygame.mixer.music.set_volume(0.1)
background_music = pygame.mixer.music.load('BoxCat_Games_CPU Talk.mp3')
pygame.mixer.music.play(-1)

#Musica bonus
music_bonus = pygame.mixer.Sound('smw_bonus_game_end.wav')

#Barulho moeda/maça
collision_noise = pygame.mixer.Sound('smw_coin.mp3')

som_morte = pygame.mixer.Sound('smw_game_over.wav')


pygame.display.set_caption('Snake Game')


width = 1280
height = 720

key_right = K_d
key_left = K_a
key_down = K_s
key_up = K_w

vel = 8
x_control = vel
y_control = 0


#Posicao inicial da cobra
x_snake = int(width/2)
y_snake = int(height/2)

#fonte do contador
font = pygame.font.SysFont('arial', 40, True, True)

#valor inicial do contador
points = 0

#posiçao inicial da maça
x_apple = randint(40, 1200)
y_apple = randint(50,700)

x_apple_green = randint(40, 1200)
y_apple_green = randint(50, 700)

x_troll_apple = randint(40, 1200)
y_troll_apple = randint(50,700)


snake_lista = []

#controla a velocidade de frames por segundo(line:81)
clock = pygame.time.Clock()

#tela do game
screen_inicio = pygame.display.set_mode((width,height))
screen = pygame.display.set_mode((width,height))

first_length = 5

inicio = True

dead = False


def x_y_apple():
    global x_apple, y_apple, x_apple_green, y_apple_green, x_troll_apple, y_troll_apple
    x_apple = randint(40 , 1200)
    y_apple = randint(50 , 700)
    x_apple_green = randint(40, 1200)
    y_apple_green = randint(50, 700)
    x_troll_apple = randint(40, 1200)
    y_troll_apple = randint(50, 700)

def death():
    global inicio, dead
    font2 = pygame.font.SysFont('arial', 20, True, True) 
    dead_msg = f'GAME OVER! Press "R" to play again!'
    text2 = font2.render(dead_msg, True, (0,0,0))
    ret_text = text2.get_rect()
    som_morte.play()
    pygame.mixer.music.set_volume(0)


    dead = True
    while dead:
        screen.fill((255,255,255))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            if event.type == KEYDOWN:
                if event.key == K_r:
                    restart_game()
                if event.key == K_m:
                    inicio = True

        ret_text.center = (width//2, height//2)
        screen.blit(text2, ret_text)
        pygame.display.update()

#Aumentando o comprimento da cobra
def increases_snake(snake_lista):
    for XeY in snake_lista:
        #XeY = [x,y]
        #XeY[0] = x
        #XeY[1] = y
        pygame.draw.rect(screen, (0,255,0), (XeY[0], XeY[1], 20, 20))
        

def restart_game():
    global points, first_length, x_snake, y_apple, y_snake, x_apple, snake_lista, head_list, dead, vel, x_apple_green, y_apple_green, vol, key_right, key_left, key_down, key_up
    points = 0
    vel = 8
    first_length = 5
    x_snake = int(width/2)
    y_snake = int(height/2) 
    x_apple = randint(40,1200) 
    y_apple = randint(50,700) 
    x_apple_green = randint(40,1200)
    y_apple_green = randint(40,700)
    snake_lista = []
    head_list = []
    dead = False
    vol = pygame.mixer.music.set_volume(0.1)
    key_right = K_d
    key_left = K_a
    key_down = K_s
    key_up = K_w
        


font3 = pygame.font.SysFont('arial', 30, True, True)
msg_inicio = "WELCOME to the snake game! Press any key to continue!"
text_inicio = font3.render(msg_inicio, True, (0,0,0))
ret_text2 = text_inicio.get_rect()



while inicio:
    screen_inicio.fill((255,255,255))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            inicio = False
            sleep(0.5)
            pygame.display.update()
    ret_text2.center = (width//2, height//2)
    screen_inicio.blit(text_inicio, ret_text2)
    pygame.display.update()
    
    
game = False


while True:
    clock.tick(30)
    screen.fill((255,255,255))
    msg = f"Pontos: {points}"
    text = font.render(msg, True, (0,0,0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        
        #Dando funçao as teclas
        if event.type == KEYDOWN:
            if event.key == key_left:
                if x_control == vel: 
                    pass
                else:
                    x_control = - vel
                    y_control = 0 
                
            if event.key == key_right:
                if x_control == - vel:
                    pass
                else:
                    x_control = + vel
                    y_control = 0

            if event.key == key_up:
                if y_control == + vel:
                    pass
                else:
                    y_control = - vel
                    x_control = 0
            if event.key == key_down:
                if y_control == - vel:
                    pass
                else:
                    y_control = + vel
                    x_control = 0

    x_snake += x_control
    y_snake += y_control

    #desenhando elementos:
    #cobra/maça
    snake = pygame.draw.rect(screen, (0,255,0), (x_snake , y_snake , 20 , 20))
    apple = pygame.draw.circle(screen, (255,0,0), (x_apple, y_apple), 15, 0)


    #criando colisao
    if snake.colliderect(apple):
        x_y_apple()
        points += 1
        if points > 0 and points % 5 == 0:
            vel += 2
            if vel >= 20:
                vel = 20
        collision_noise.play()
        if points == 50:
            music_bonus.play()  
        first_length += 1

    if points >= 15:
        apple_green = pygame.draw.circle(screen,(0,255,0), (x_apple_green, y_apple_green), points*1.5, 0)
        if apple_green.colliderect(apple):
            x_y_apple()
        if snake.colliderect(apple_green):
            death()

    if points >= 30:
        troll_apple = pygame.draw.circle(screen, (70, 41, 90), (x_troll_apple, y_troll_apple), 15, 0)
        if troll_apple.colliderect(apple_green):
            x_y_apple()

        elif troll_apple.colliderect(apple):
            x_y_apple()

        if snake.colliderect(troll_apple):
            key_left, key_right = key_right, key_left
            key_up, key_down = key_down, key_up
            x_y_apple()       
            

    #armazenando os valores X e Y da "cobra"
    head_list = []
    head_list.append(x_snake)
    head_list.append(y_snake)

    if len(snake_lista) > first_length:
        del snake_lista[0]
    
    #aramazenado o valor que a "head_list" adiquirir
    snake_lista.append(head_list)
    
    #tela de morte
    if snake_lista.count(head_list) > 1 or x_snake > width or x_snake < 0 or y_snake > height or y_snake < 0: #se tiver duas coodernadas iguais uma da cabeça e outra do corpo a cobra encostou em si mesma
        death()

    #funçao que faz a cobra crescer
    increases_snake(snake_lista)

    #escrevendo o contador de pontos
    screen.blit(text, (width - 224,40))


    pygame.display.flip()
