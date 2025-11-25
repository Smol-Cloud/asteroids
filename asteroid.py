from circleshape import CircleShape
import pygame
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)
    
    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        # Immediately .kill() itself (think about it: this asteroid is always destroyed, but maybe we'll spawn new smaller ones, depending on its size).
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")

        split_degrees = random.uniform(20, 50)

        first_asteroid_movement = self.velocity.rotate(split_degrees)
        second_asteroid_movement = self.velocity.rotate(-split_degrees)

        created_asteroid_radius = self.radius - ASTEROID_MIN_RADIUS

        first_asteroid = Asteroid(self.position.x, self.position.y, created_asteroid_radius)
        second_asteroid = Asteroid(self.position.x, self.position.y, created_asteroid_radius)

        first_asteroid.velocity = first_asteroid_movement * 1.2
        second_asteroid.velocity = second_asteroid_movement * 1.2


