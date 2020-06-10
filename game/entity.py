from glm import vec2
import pygame


class Entity:
    def __init__(self, pos: vec2, mass):
        self.pos: vec2 = pos
        self.mass = mass
        self.vel: vec2 = vec2(0)

        self.radius = (mass ** 0.5) * 5
        self.rect = (self.pos.x - self.radius, self.pos.y - self.radius, self.radius * 2, self.radius * 2)
        self.color = (0, 0, 0)

    def update(self, dt):
        self.pos += self.vel * dt

    def render(self, window):
        pygame.draw.ellipse(window, self.color, self.rect)
