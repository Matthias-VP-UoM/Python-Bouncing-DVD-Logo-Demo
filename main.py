# Importing pygame and random packages
import random
import pygame

# Pygame setup
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("DVD Bouncing Screen Template")
clock = pygame.time.Clock()
running = True

# Other variables
dt = 0
previous_index = index = 0

# Boolean values
changed_colour = False

# Colours
WHITE = (255,255,255)
BLACK = (0,0,0)
GREY = (128,128,128)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
CYAN = (0,255,255)
YELLOW = (255,255,0)
GOLD = 	(255,215,0)
ORANGE = (255,165,0)
BROWN = (165,42,42)
PURPLE = (160,32,240)
PINK = (255,192,203)

# Array containing list of colours - used when changing colour of rectangle
COLOURS_ARRAY = [WHITE, RED, GREY, GREEN, BLUE, CYAN, YELLOW, GOLD, ORANGE, BROWN, PURPLE, PINK]

# Rectangle variables
# Starting position
rect_pos_x = screen.get_width()/2
rect_pos_y = screen.get_height()/2

# Dimensions
rect_width = 150
rect_height = 100

# Movement speed
rect_speed_x = 200
rect_speed_y = 200

def switch_colour():
    global changed_colour, previous_index, index
    while previous_index == index:
        index = random.randint(0,len(COLOURS_ARRAY)-1)
    changed_colour = True

# Game Loop
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill(BLACK)

    # RENDER YOUR GAME HERE
    # Set colour of rectangle
    # If statement is used to prevent rapid changing of colours
    if not changed_colour:
        index = random.randint(0,len(COLOURS_ARRAY)-1)
        changed_colour = True
    
    # Set previous index to current index
    previous_index = index

    # Draw rectangle using details given
    pygame.draw.rect(screen, COLOURS_ARRAY[index], (rect_pos_x, rect_pos_y, rect_width, rect_height))

    # Move the rectangle according to speed given
    rect_pos_x += rect_speed_x * dt
    rect_pos_y += rect_speed_y * dt

    # Collision detection
    if (rect_pos_x >= screen.get_width() - rect_width):
        changed_colour = False

        # Change colour
        if not changed_colour:
            rect_speed_x *= -1
            switch_colour()
        
        previous_index = index
    elif (rect_pos_x <= 0):
        changed_colour = False

        # Change colour
        if not changed_colour:
            rect_speed_x *= -1
            switch_colour()
        
        previous_index = index
    
    if (rect_pos_y >= screen.get_height() - rect_height):
        changed_colour = False

        # Change colour
        if not changed_colour:
            rect_speed_y *= -1
            switch_colour()
        
        previous_index = index
    elif (rect_pos_y <= 0):
        changed_colour = False

        # Change colour
        if not changed_colour:
            rect_speed_y *= -1
            switch_colour()
        
        previous_index = index

    # flip() the display to put your work on screen
    pygame.display.flip()

    # Set FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()