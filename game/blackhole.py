from glm import vec2
import pygame

from game.entity import Entity


class BlackHole(Entity):
    def render(self, window):
        super().render(window)
        border = round(self.radius / 6)
        pygame.draw.circle(window, (244, 136, 13), self.pos, self.radius, border)
