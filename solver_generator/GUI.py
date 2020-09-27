#WORK UNDER PROGRESSION

import pygame
pygame.init()

#create the screen
screen = pygame.display.set_mode((600,600))
font = pygame.font.Font("freesansbold.ttf", 16)
#title and icon
pygame.display.set_caption("Sudoku")
pygame.display.set_icon(pygame.image.load("images/sudoku_icon.png"))

def displayy():
    screen.blit(pygame.image.load("images/sudoku_index.png"), (75,190))
    screen.blit(pygame.image.load("images/logo0.png"), (-30,0))

#game loop
running = True
while running:
    screen.fill((255,255,255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False    
    displayy()
    pygame.display.update()




