import sys
import pygame
from globals.python_defaults import colors
from final_project import player
from final_project import block
from final_project import tilemap

pygame.init()

done = False
clock = pygame.time.Clock()

screen_size = {"x": 1160, "y": 800}
screen = pygame.display.set_mode((screen_size["x"], screen_size["y"]))
pygame.display.set_caption("unit-04: Images and Surfaces")
tile_size = {"x": 40, "y": 40}

the_player = player.Player(tile_size)
player_list = pygame.sprite.Group()
player_list.add(the_player)

level_map = tilemap.Map(screen_size, tile_size)
tile_group = pygame.sprite.Group()

longest = 0
start_position = tile_size["x"] * 10

for level in level_map.levels:
    
    longest = max(len(level_map.levels[level]), longest)

for level in level_map.levels:
    
        previous_image = 0
        
        for count, tile in list(enumerate(level_map.levels[level])):
            if tile == "x":
                
                if count == 0:
                    start_position = 0
                    iterations = 11
                else:
                    iterations = longest
                    start_position = tile_size["x"] * 10
                
                for filler_tile in range(count, iterations):
                    map_tile = block.Block(previous_image, (tile_size["x"], tile_size["y"]))
                    map_tile.rect.x = (filler_tile * (tile_size["x"])) + start_position
                    map_tile.rect.bottom = screen_size["y"] - level * (tile_size["y"])

                    tile_group.add(map_tile)

            else:
                start_position = tile_size["x"] * 10
                
                map_tile = block.Block(tile, (tile_size["x"], tile_size["y"]))
                map_tile.rect.x = (count * (tile_size["x"])) + start_position
                map_tile.rect.bottom = screen_size["y"] - level * (tile_size["y"])

                tile_group.add(map_tile)

            previous_image = tile

while not done:
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            done = True
    
    pressed = pygame.key.get_pressed()
    the_player.process_user_input(pressed, screen_size)

    screen.fill(colors.BLUE)

    tile_group.draw(screen)

    the_player.run(screen_size)
    player_list.draw(screen)

    pygame.display.update()
    
    clock.tick(60)

pygame.quit()
sys.exit()