from glm import vec2
import pygame

from game.entity import Entity


class Planet(Entity):
    def __init__(self, pos: vec2, mass, color):
        super().__init__(pos, mass)
        self.color = color
