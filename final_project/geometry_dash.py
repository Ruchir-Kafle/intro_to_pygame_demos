import sys
import pygame
from globals.python_defaults import colors
from final_project import win_screen
from final_project import player
from final_project import map

pygame.init()

done = False
clock = pygame.time.Clock()

screen_size = {"x": 1160, "y": 800}
screen = pygame.display.set_mode((screen_size["x"], screen_size["y"]))
pygame.display.set_caption("Final Project: Geometry Dash")
tile_size = {"x": 40, "y": 40}

player_group = pygame.sprite.Group()

the_player = player.Player(tile_size=tile_size, screen_size=screen_size)
player_group.add(the_player)

the_map = map.Map(tile_size=tile_size, screen_size=screen_size)

the_win_screen = win_screen.Win_Screen(screen_size=screen_size)
won = False

while not done:
    for event in pygame.event.get():    
        if event.type == pygame.QUIT:
            done = True

    if not the_player.player_offset >= the_map.farthest:
        if not won:
            won = True
            screen.fill(colors.WHITE)
            screen.blit(the_win_screen.screen, (0, 0))
    else:
        background = pygame.transform.scale(pygame.image.load("final_project/assets/background.png"), (screen_size["x"], screen_size["y"]))
        
        the_map.update_map(player=the_player)

        pressed = pygame.key.get_pressed()
        the_player.process_user_input(pressed)

        current_collisions = pygame.sprite.spritecollide(the_player, the_map.tile_group, False)
        the_player.run(collisions=current_collisions)

        screen.blit(background, (0, 0))
        the_map.tile_group.draw(screen)
        player_group.draw(screen)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
sys.exit()