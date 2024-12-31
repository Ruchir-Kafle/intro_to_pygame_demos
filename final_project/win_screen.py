import pygame
from globals.python_defaults import colors
from final_project import play_again_button
from globals.python_defaults import fonts

class Win_Screen():
    def __init__(self, screen_size):
        self.button_group = pygame.sprite.Group()
        
        color = (*colors.BLACK, 50)

        self.screen = pygame.Surface((screen_size["x"], screen_size["y"]), pygame.SRCALPHA)
        self.screen.fill(color)

        font = pygame.font.SysFont(fonts.ARIAL, 70)

        play_again_button.Play_Again_Button(size={"x": 400, "y": 100}, coordinates={"x": 0, "y": 0}, group=self.button_group, color=colors.BLUE, text="Play Again", font=font)

        self.update()

    def update(self, click=False, player=None):
        for button in self.button_group:
            button.hover(clicked=click, player=player)

        self.button_group.draw(self.screen)