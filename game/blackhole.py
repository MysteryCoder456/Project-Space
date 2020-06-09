from glm import vec2
import pygame


class BlackHole:
    def __init__(self, pos: vec2, mass):
        self.pos = pos
        self.mass = mass
        self.radius = (mass ** 0.5) * 5

    def render(self, window):
        rect = (self.pos.x - self.radius, self.pos.y - self.radius, self.radius * 2, self.radius * 2)
        border = self.mass // 6
        pygame.draw.ellipse(window, (0, 0, 0), rect)
        pygame.draw.ellipse(window, (244, 136, 13), rect, border)
