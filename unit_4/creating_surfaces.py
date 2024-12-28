# Importing modules.
import sys
import pygame
from globals.python_defaults import player
from globals.python_defaults import colors

# Pygame must be initialized before running.
pygame.init()

# Boilerplate variables.
# When done is true, the loop will end.
done = False

# A clock, registers the games' ticks and sets a cap on frames per second (fps).
clock = pygame.time.Clock()

# Creating a window
# Screen size.
screen_size = {"x": 1000, "y": 700}

# Creating the actual screen.
screen = pygame.display.set_mode((screen_size["x"], screen_size["y"]))

# Giving the screen a name.
pygame.display.set_caption("unit-04: Images and Surfaces")

# Player variables, DO NOT TOUCH!
the_player = player.Player(screen_size)
player_list = pygame.sprite.Group()
player_list.add(the_player)

# Main loop. Everything you want to happen in the game is put in this loop.
while not done:

    # Looping through every possible event that the user can get in Pygame.
    for event in pygame.event.get():
        
        # If the user presses the "X" button in the top right corner, done will be set to true, ending the loop, and thus the game.
        if event.type == pygame.QUIT:
            done = True
    
    # Getting user input.
    pressed = pygame.key.get_pressed()
    the_player.process_user_input(pressed, screen_size)

    # Setting the screen to a black background. Try changing the color from BLACK to something else!
    screen.fill(colors.BLACK)

    # Type out your code below! Let's make a basic surface and then an image surface!
    block = pygame.Surface((200, 200))
    block.fill(colors.RED)
    screen.blit(block, (screen_size["x"] - block.get_width() - 50, screen_size["y"] - block.get_height()))

    image = pygame.image.load("unit_4/do_not_touch/geometry_dash_block.png").convert_alpha()
    screen.blit(image, (50, screen_size["y"] - image.get_height()))

    # Player functions, DO NOT TOUCH.
    the_player.run(screen_size)
    player_list.draw(screen)

    # End commands.
    # Rendering the game.
    pygame.display.update()
    
    # Capping the ticks, and thus the fps, to 60.
    clock.tick(60)

# Ending the game when the loop is finished. These commands actually end Pygame. If the loop ends and these commands are not here, the game will not actually end.
pygame.quit()
sys.exit()