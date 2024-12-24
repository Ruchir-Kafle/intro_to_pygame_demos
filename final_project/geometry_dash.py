import sys
import pygame
from final_project import player
from final_project import create_map

pygame.init()

done = False
clock = pygame.time.Clock()

screen_size = {"x": 1160, "y": 800}
screen = pygame.display.set_mode((screen_size["x"], screen_size["y"]))
pygame.display.set_caption("Final Project: Geometry Dash")
tile_size = {"x": 40, "y": 40}

player_group = pygame.sprite.Group()
tile_group = pygame.sprite.Group()

the_player = player.Player(tile_size, screen_size)
player_group.add(the_player)

map = create_map.Map(tile_size, screen_size, tile_group)

while not done:
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            done = True
    
    pressed = pygame.key.get_pressed()
    the_player.process_user_input(pressed)

    background = pygame.transform.scale(pygame.image.load("final_project/assets/background.png"), (screen_size["x"], screen_size["y"]))
    screen.blit(background, (0, 0))

    for block in tile_group:
        block.rect.x = block.initial_x
        block.rect.x -= the_player.player_offset

    tile_group.draw(screen)

    current_collisions = pygame.sprite.spritecollide(the_player, tile_group, False)

    the_player.run(current_collisions)

    if the_player.player_offset >= map.farthest:
        the_player.trigger_death()

    player_group.draw(screen)

    pygame.display.update()
    
    clock.tick(60)

pygame.quit()
sys.exit()