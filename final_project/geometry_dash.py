import sys
import pygame
from globals.python_defaults import colors
from final_project import win_screen
from final_project import player
from final_project import map

class Game():
    def __init__(self):
        pygame.init()

        self.done = False
        self.clock = pygame.time.Clock()

        self.screen_size = {"x": 1160, "y": 800}
        self.screen = pygame.display.set_mode((self.screen_size["x"], self.screen_size["y"]))
        pygame.display.set_caption("Final Project: Geometry Dash")
        self.tile_size = {"x": 40, "y": 40}

        self.player_group = pygame.sprite.Group()

        self.the_player = player.Player(tile_size=self.tile_size, screen_size=self.screen_size)
        self.player_group.add(self.the_player)

        self.the_map = map.Map(tile_size=self.tile_size, screen_size=self.screen_size)

        self.the_win_screen = win_screen.Win_Screen(screen_size=self.screen_size)
        self.won = False

    def user_input(self):
        for event in pygame.event.get():    
            if event.type == pygame.QUIT:
                self.done = True
            if event.type == pygame.MOUSEBUTTONUP:
                play_again = False

                for button in self.the_win_screen.button_group:
                    play_again = (play_again or button.hover(clicked=True, player=self.the_player))

                if play_again:
                    self.won = False

    def update_components(self):
        if not self.won:
            self.the_map.update_map(player=self.the_player)

            pressed = pygame.key.get_pressed()
            self.the_player.process_user_input(pressed=pressed)

            current_collisions = pygame.sprite.spritecollide(self.the_player, self.the_map.tile_group, False)
            self.the_player.run(collisions=current_collisions)

    def draw(self):
        self.screen.blit(self.background, (0, 0))
        self.the_map.tile_group.draw(self.screen)
        self.player_group.draw(self.screen)

    def check_for_win(self):
        if self.the_player.player_offset >= self.the_map.farthest or self.won:
            self.won = True

            self.the_win_screen.update()

            self.screen.blit(self.the_win_screen.screen, (0, 0))

    def run(self):
        while not self.done:
            self.background = pygame.transform.scale(pygame.image.load("final_project/assets/background.png"), (self.screen_size["x"], self.screen_size["y"]))

            self.user_input()

            self.update_components()

            self.draw()

            self.check_for_win()

            pygame.display.update()
            self.clock.tick(60)

        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    game = Game()
    game.run()