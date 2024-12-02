# Importing Pygame.
import pygame

# Pygame must be initialized before running.
pygame.init()

# Boilerplate variables.
# When done is true, the loop will end.
done = False

# A clock, registers the games' ticks and sets a cap on frames per second (fps).
clock = pygame.time.Clock()

# Creating a window
# Screen size.
screen_size = (700, 500) 

# Creating the actual screen.
screen = pygame.display.set_mode(screen_size)

# Giving the screen a name.
pygame.display.set_caption("unit-01: Introduction to Boilerplate")

# Main loop. Everything you want to happen in the game is put in this loop.
while not done:

    # Looping through every possible event that the user can get in Pygame.
    for event in pygame.event.get():
        
        # If the user presses the "X" button in the top right corner, done will be set to true, ending the loop, and thus the game.
        if event.type == pygame.QUIT:
            done = True

    # Setting the screen to a black background.
    screen.fill((0, 0, 0))

    # End commands.
    # Rendering the game.
    pygame.display.flip()
    
    # Capping the ticks, and thus the fps, to 60.
    clock.tick(60)

# Ending the game when the loop is finished. This command is the one that actually ends Pygame. If the loop ends and this command is not here, the game will not actually end.
pygame.quit()