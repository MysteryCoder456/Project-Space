import pygame
from glm import vec2

from game.blackhole import BlackHole


class Game:
    def __init__(self, w, h):
        self.width, self.height = w, h
        self.win = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Project Space")
        self.background = pygame.Color("black")

        self.bl = BlackHole(vec2(w / 2, h / 2), 50)

    def mouse_down(self, pos):
        print("down:", pos)

    def mouse_up(self, pos):
        print("up:", pos)

    def update(self, dt):
        pass

    def render(self, window):
        window.fill(self.background)

        self.bl.render(window)

        pygame.display.update()
