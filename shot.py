from constants import *
from circleshape import *
import pygame


class Shot(CircleShape):
    def __init__(self, x, y, rotation):
        super().__init__(x, y, 5)
        self.velocity = pygame.Vector2(0, 1).rotate(rotation) * PLAYER_SHOT_SPEED

    def update(self, dt):
        self.position += self.velocity * dt

    def draw(self, screen):
        pygame.draw.circle(screen, 'red', self.position, self.radius)