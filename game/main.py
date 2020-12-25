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

        # self.bl = BlackHole(vec2(w - 450, h / 2), 50)
        # self.bl.vel += vec2(0, 300)

        self.p1 = Planet(vec2(w / 2 - 100, h / 2), 45, (200, 200, 200))
        # self.p1.vel += vec2(0, -25)

        self.p2 = Planet(vec2(w - 150, h / 2), 15, (200, 200, 200))
        self.p2.vel += vec2(0, 75)

    def mouse_down(self, pos):
        print("down:", pos)

    def mouse_up(self, pos):
        print("up:", pos)

    def update(self, dt):
        self.p1.attract_towards(self.p2)
        self.p2.attract_towards(self.p1)

        self.p1.update(dt)
        self.p2.update(dt)
        # self.bl.update(dt)

        if self.p1.is_colliding(self.p2):
            self.p1.collide(self.p2)
            self.p2.collide(self.p1)

    def render(self, window):
        window.fill(self.background)

        # self.bl.render(window)
        self.p1.render(window)
        self.p2.render(window)

        pygame.display.update()
