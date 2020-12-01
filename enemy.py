import pygame
import random


class Enemy:
    def __init__(self, pos, surface):
        speeds = [-3, -2, -1, 1, 2, 3]
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.x_velocity = random.choice(speeds)
        self.y_velocity = random.choice(speeds)
        self.radius = 5
        self.color = pygame.Color('red')
        self.surface = surface

    # draws enemy
    def draw(self):
        pygame.draw.circle(self.surface, self.color, (self.x_pos, self.y_pos), self.radius)

    # updates enemy position
    def move(self):
        self.x_pos += self.x_velocity
        self.y_pos += self.y_velocity

        if self.x_pos <= 0 or self.x_pos >= self.surface.get_width():
            self.x_velocity *= -1
        if self.y_pos <= 0 or self.y_pos >= self.surface.get_height():
            self.y_velocity *= -1

    # returns position of self
    def get_position(self):
        return self.x_pos, self.y_pos
