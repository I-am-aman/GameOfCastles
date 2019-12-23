import pygame
from pygame.locals import *

# Initialize the game
pygame.init()
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
keys = [False, False, False, False]
playerpos = [100, 100]

# Load images
player = pygame.image.load("resources/images/dude.png")
grass = pygame.image.load("resources/images/grass.png")
castle = pygame.image.load("resources/images/castle.png")

# keep looping through
while 1:
    # Clear the screen before drawing it again
    screen.fill(0)
    # Draw the screen elements
    for x in range(width/grass.get_width()+1):
        for y in range(height/grass.get_height()+1):
            screen.blit(grass, (x*100, y*100))
    screen.blit(castle, (0, 30))
    screen.blit(castle, (0, 135))
    screen.blit(castle, (0, 240))
    screen.blit(castle, (0, 345))
    screen.blit(player, playerpos)
    # Update the screen
    pygame.display.flip()
    # Loop through the events
    for event in pygame.event.get():
        # Check if the event is the X button
        if event.type == pygame.QUIT:
            # if it is quit the game
            pygame.quit()
            exit(0)
