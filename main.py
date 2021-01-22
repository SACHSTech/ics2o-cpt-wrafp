""" 
Name: main.py
Purpose: To create a short and basic game which displays information about hardware and protection from viruses. 
         Then when the game ends, there will be a quiz which tests the knowledge that was previously shown.

Author: Huang.K

Created:    date: 26/1/2021
"""
 
import pygame
 
# Function for the character
# Define a function that will draw a stickman at a certain location
# player = 
    

# Define some colors
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
VIOLET   = ( 120,  42, 199)
PURPLE   = (  79,  18, 140)
 
pygame.init()
  
# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("My Game")
 
#Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

pygame.mouse.set_visible(0)

background_image = pygame.image.load("background.png").convert()
player_image = pygame.image.load("character_robot_idle.png").convert()

x_coord = 10
y_coord = 10

x_speed = 0
y_speed = 0

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop
  
        # Create an if statement that gives instructions
        # When a key is pressed (in this case: movement)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a or pygame.K_LEFT:
                x_speed = -3
            if event.key == pygame.K_d or pygame.K_RIGHT:
                x_speed = 4
            if event.key == pygame.K_w or pygame.K_UP:
                y_speed = -3
            if event.key == pygame.K_s or pygame.K_DOWN:
                y_speed = 3

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a or pygame.K_LEFT:
                x_speed = 0
            if event.key == pygame.K_d or pygame.K_RIGHT:
                x_speed = 0
            if event.key == pygame.K_w or pygame.K_UP:
                y_speed = 0
            if event.key == pygame.K_s or pygame.K_DOWN:
                y_speed = 0

    # --- Game logic should go here
    x_coord += x_speed
    y_coord += y_speed


    # --- Drawing code should go here
     
    # First, clear the screen to white or whatever background colour. 
    # Don't put other drawing commands above this, or they will be erased with this command.
    # blit takes a image in memory and loads it
    screen.blit(background_image, [0, 0])
    screen.blit(player_image, [20, 500])
     
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(20)
      
# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.
pygame.quit()