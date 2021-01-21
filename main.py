""" 
A basic pygame template
"""
 
import pygame
 
# Function for the character
# Define a function that will draw a stickman at a certain location
def draw_stick_figure(screen, x, y):
    # Head
    pygame.draw.ellipse(screen, PURPLE, [x, y, 10, 10], 0)
    pygame.draw.ellipse(screen, VIOLET, [18+x, 10+y, 15, 15], 0)
    pygame.draw.ellipse(screen, VIOLET, [-14+x, 6+y, 14, 18], 0)

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

pygame.image.load("character.png")
 
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop
  
    # --- Game logic should go here
    pos = pygame.mouse.get_pos()
    x = pos[0]
    y = pos[1]
    # --- Drawing code should go here
     
    # First, clear the screen to white or whatever background colour. 
    # Don't put other drawing commands above this, or they will be erased with this command.
    screen.fill(WHITE)
    draw_stick_figure(screen, x, y)
     
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
     
# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.
pygame.quit()