import pygame
from glm import vec2

from game.blackhole import BlackHole
from game.planet import Planet


class Game:
    def __init__(self, w, h):
        self.width, self.height = w, h
        self.win = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Project Space")
        self.background = pygame.Color("black")

        self.bl = BlackHole(vec2(w / 2, h / 2), 50)
        self.planet = Planet(vec2(300, h / 2), 10, (200, 200, 200))
        self.planet.vel += vec2(0, 0.2)

    def mouse_down(self, pos):
        print("down:", pos)

    def mouse_up(self, pos):
        print("up:", pos)

    def update(self, dt):
        self.planet.attract_towards(self.bl)
        self.planet.update(dt)

    def render(self, window):
        window.fill(self.background)

        self.bl.render(window)
        self.planet.render(window)

        pygame.display.update()
