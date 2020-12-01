import pygame


class Player:
    def __init__(self, pos, surface):
        self.surface = surface
        self.color = pygame.Color((100, 100, 255))
        self.radius = 5
        self.x_pos = pos[0]
        self.y_pos = pos[1]

    # draws player
    def draw(self):
        pygame.draw.circle(self.surface, self.color, (self.x_pos, self.y_pos), self.radius)

    # updates position of player
    def move(self, pos):
        self.x_pos = pos[0] if 0 <= pos[0] <= self.surface.get_width() else self.x_pos
        self.y_pos = pos[1] if 0 <= pos[1] <= self.surface.get_height() else self.y_pos

    # returns true if player is colliding with an enemy e
    def collide(self, e):
        enemy_pos = e.get_position()
        return self.x_pos in range(enemy_pos[0]-5, enemy_pos[0]+5) and self.y_pos in range(enemy_pos[1]-5, enemy_pos[1]+5)