import pygame
from globals.python_defaults import colors
from final_project import button
from globals.python_defaults import fonts

class Win_Screen():
    def __init__(self, screen_size):
        self.button_group = pygame.sprite.Group()
        
        color = (*colors.BLACK, 50)

        self.screen = pygame.Surface((screen_size["x"], screen_size["y"]), pygame.SRCALPHA)
        self.screen.fill(color)

        font = pygame.font.SysFont(fonts.ARIAL, 70)

        button.Button(size={"x": 400, "y": 100}, coordinates={"x": 0, "y": 0}, group=self.button_group, color=colors.BLUE, text="Play Again", font=font)

        # Text with multiple buttons doesn't seem to be working, revisit later if necessary.
        # button.Button(size={"x": 400, "y": 100}, coordinates={"x": 0, "y": 150}, group=self.button_group, color=colors.BLUE, text="Play Again", font=font)

        # button.Button(size={"x": 400, "y": 100}, coordinates={"x": 0, "y": 300}, group=self.button_group, color=colors.BLUE, text="Play Again", font=font)

        self.update()

    def update(self, click=False):
        for button in self.button_group:
            button.hover(click)

        self.button_group.draw(self.screen)