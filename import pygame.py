import pygame
from pygame.locals import *
from sys import exit

pygame.init()

width = 640
height = 480

black = (0,0,0)

screen = pygame.display.set_mode((width,height))
pygame.display.set_caption('Game frog')



class Frog(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.image.load('sprites/attack_1.png'))
        self.sprites.append(pygame.image.load('sprites/attack_2.png'))
        self.sprites.append(pygame.image.load('sprites/attack_3.png'))
        self.sprites.append(pygame.image.load('sprites/attack_4.png'))
        self.sprites.append(pygame.image.load('sprites/attack_5.png'))
        self.sprites.append(pygame.image.load('sprites/attack_6.png'))
        self.sprites.append(pygame.image.load('sprites/attack_7.png'))
        self.sprites.append(pygame.image.load('sprites/attack_8.png'))
        self.sprites.append(pygame.image.load('sprites/attack_9.png'))
        self.sprites.append(pygame.image.load('sprites/attack_10.png'))
        self.atual = 0
        self.image = self.sprites[self.atual]
        self.image = pygame.transform.scale(self.image, (128*3, 64*3))

        self.rect = self.image.get_rect()
        self.rect.topleft = 100, 10

        self.animar = False
    
    def attack(self):
        self.animar = True


    def update(self):
        if self.animar == True:
            self.atual = self.atual + 0.5
            if self.atual > len(self.sprites) - 1:
                self.atual = 0
                self.animar = False
            self.image = self.sprites[int(self.atual)]
            self.image = pygame.transform.scale(self.image, (128*3, 64*3))



all_sprites = pygame.sprite.Group()
frog = Frog()

clock = pygame.time.Clock()

all_sprites.add(frog)


while True:
    clock.tick(30)
    screen.fill(black)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit
            exit()
        if event.type == KEYDOWN:
            frog.attack()

    all_sprites.draw(screen)
    all_sprites.update()
    pygame.display.flip()