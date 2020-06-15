from glm import vec2
import pygame

from game.entity import Entity


class Planet(Entity):
    def __init__(self, pos: vec2, mass, color):
        """
        Planet Body

        Args:
            pos (vec2): initial position,
            mass (float/int): mass of body,
            color (tuple/pygame.Color): color of the planet
        """

        super().__init__(pos, mass)
        self.color = color

    def collide(self, entity: Entity):
        mul1 = 0.93
        new_vel_1 = vec2(
            (self.vel.x * (self.mass - entity.mass) + (2 * entity.mass * entity.vel.x)) / (self.mass + entity.mass),
            (self.vel.y * (self.mass - entity.mass) + (2 * entity.mass * entity.vel.y)) / (self.mass + entity.mass)
        ) * mul1
        new_vel_2 = vec2(
            (entity.vel.x * (entity.mass - self.mass) + (2 * self.mass * self.vel.x)) / (entity.mass + self.mass),
            (entity.vel.y * (entity.mass - self.mass) + (2 * self.mass * self.vel.y)) / (entity.mass + self.mass)
        ) * mul1

        mul2 = 0.7

        self.pos += new_vel_1 / self.radius * mul2
        entity.pos += new_vel_2 / entity.radius * mul2

        self.vel = new_vel_1
        entity.vel = new_vel_2
