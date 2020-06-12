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

        self.bl = BlackHole(vec2(w - 450, h / 2), 50)
        self.bl.vel += vec2(0, 300)

        self.planet = Planet(vec2(450, h / 2), 50, (200, 200, 200))
        self.planet.vel += vec2(0, -300)

    def mouse_down(self, pos):
        print("down:", pos)

    def mouse_up(self, pos):
        print("up:", pos)

    def update(self, dt):
        self.planet.attract_towards(self.bl)
        self.bl.attract_towards(self.planet)

        self.planet.update(dt)
        self.bl.update(dt)

    def render(self, window):
        window.fill(self.background)

        self.bl.render(window)
        self.planet.render(window)

        pygame.display.update()
