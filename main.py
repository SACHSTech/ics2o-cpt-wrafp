""" 
Name: main.py
Purpose: To create a short and basic game which displays information about hardware and protection from viruses. 
         
Author: Huang.K

Created:    date: 27/1/2021
"""
 
import pygame
import random
import time

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

pygame.display.set_caption("Computer Studies Practice Quiz #5125")
 
#Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Used to set the mouse invisible
pygame.mouse.set_visible(0)

# Loading images 
background_image = pygame.image.load("background.png").convert()
player_image = pygame.image.load("character_robot_idle.png").convert()

player_image.set_colorkey(BLACK)

# List of variables
x_start_pos = 50
y_start_pos = 50

x_value = 50
y_value = 100

x_coord = 10
y_coord = 10

x_speed = 0
y_speed = 0

number_of_clicks = 0
hit_points = 20

score = 0

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

        # When the LMB is clicked equal to the hit_points variable, it will load up a practice quiz which can then be accessed through a passcode
        # If statements will update your score which at the end is calculated to show how ready you are for an upcoming examination
        if event.type == pygame.MOUSEBUTTONDOWN:
            hit_points = hit_points - 1
            if hit_points <= 0:
                screen.blit(background_image, [0, 0])
                passcode_question = input("Enter passcode: ")
                if passcode_question == "ycdsb":
                    time.sleep(2)
                    print("Loading...")
                    time.sleep(2)
                    question_1 = int(input("\nQ1: RAM stands for? \na) Random Access Monitor(1)\nb) Remote Access Memory(2) \nc) Random Access Memory(3) \nd) Random Accustomed Memory(4)\n"))
                    time.sleep(3)
                    if question_1 == 3:
                        score = score + 10
                        print("Correct! your score is", score)
                    else:
                        print("Incorrect. your score is", score)

                    time.sleep(1.5)
                    question_2 = int(input("\nQ2: What is the Memory Hierachy? \na) Chip Memory->External Memory->Storage(1) \nb) Chip Memory->Storage->External Memory(2) \nc) External Memory->Chip Memory->Storage(3)\n"))
                    time.sleep(3)
                    if question_2 == 1:
                        score = score + 10
                        print("Correct! your score is", score)
                    else:
                        print("Incorrect. your score is", score)

                    time.sleep(1.5)
                    question_3 = int(input("\nQ3: What is the unit of measure for connection speed? \na) Byte(1) \nb) Bits(2) \nc) DPI(3) \nd) PPI(4)\n"))
                    time.sleep(3)
                    if question_3 == 2:
                        score = score + 10
                        print("Correct! your score is", score)
                    else:
                        print("Incorrect. your score is", score)
                
                    time.sleep(1.5)
                    question_4 = int(input("\nQ4: What is an Operating System? \na) A macro program(1) \nb) A mouse or a keyboard(2) \nc) A system that helps organizes your files and stores information(3) \nd) Software that manages4
                     hardware and software; and includes services(4)\n"))
                    time.sleep(3)
                    if question_4 == 4:
                        score = score + 10
                        print("Correct! your score is", score)
                    else:
                        print("Incorrect. your score is", score)

                    time.sleep(1.5)
                    question_5 = int(input("\nQ5: Which of the following is not a preventative measure in avoiding malware? \na) Install antivirus software(1) \nb) Dont click on questionable links(2) \nc) Download pirated software(3)\n"))
                    time.sleep(3)
                    if question_5 == 3:
                        score = score + 10
                        print("Correct! your score is", score)
                    else:
                        print("Incorrect. your score is", score)

                    time.sleep(1.5)
                    question_6 = int(input("\nQ6: What word doesn't describe a rootkit? \na) Dangerous(1) \nb) Cloning(2) \nc) Hidden(3) \nd) Control(4)\n"))
                    time.sleep(3)
                    if question_6 == 2:
                        score = score + 10
                        print("Correct! your score is", score)
                    else:
                        print("Incorrect. your score is", score)

                    time.sleep(1.5)
                    question_7 = int(input("\nQ7: What error type describes having incorrect grammar rules/incorrect execution in programming? \na) Logical Error(1) \nb) Syntax Error(2) \nc) Run Time Error(3) \nd) Grammar Error(4)\n2
                    "))
                    time.sleep(3)
                    if question_7 == 2:
                        score = score + 10
                    print("Calculating...")
                    time.sleep(5)
                    if score >= 60:
                        print("\nYou know your material, Good Job! \nScore:", score)
                    elif score >= 40 and score <= 59:
                        print("\n You need more studying. \nScore:", score)
                    elif score >= 11 and score <= 39:
                        print("Better study... ಠ_ಠ \nScore:", score)
                    else:
                        print("Time to cram! \nScore:", score)

                else:
                    print("==[Incorrect Passcode]==")

 
    # --- Game logic should go here
    x_coord += x_speed
    y_coord += y_speed


    # --- Drawing code should go here
     
    # First, clear the screen to white or whatever background colour. 
    # Don't put other drawing commands above this, or they will be erased with this command.
    # blit takes a image in memory and loads it
    screen.blit(background_image, [0, 0])
    screen.blit(player_image, [x_coord, y_coord])

    # The font to use, size, bold, italics
    font = pygame.font.SysFont('Calibri', 25, True, False)
    # Creates the text but is saved in memory
    text = font.render("Click 20 times to verify you are human.",True,WHITE)
    # Stamps on the text at the x and y coords
    screen.blit(text, [150, 250])

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(20)
      
# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.
pygame.quit()