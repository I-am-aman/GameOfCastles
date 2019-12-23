import pygame
from pygame.locals import *

# Initialize the game
pygame.init()
width, height = 640, 480
screen = pygame.display.set_mode((width, height))

# Load images
player = pygame.image.load("resources/images/dude.png")

# keep looping through
while 1:
    # Clear the screen before drawing it again
    screen.fill(0)
    # Draw the screen elements
    screen.blit(player, (100, 100))
    # Update the screen
    pygame.display.flip()
    # Loop through the events
    for event in pygame.event.get():
        # Check if the event is the X button
        if event.type == pygame.QUIT:
            # if it is quit the game
            pygame.quit()
            exit(0)
