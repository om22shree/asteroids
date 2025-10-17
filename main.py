import pygame
from constants import *
from player import *
from asteroid import *
from asteroidField import *
from shot import *

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroidable = pygame.sprite.Group()
    AsteroidField.containers = updatable

    Asteroid.containers = updatable, drawable, asteroidable
    Player.containers = updatable, drawable
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidField = AsteroidField()
    Shot.containers = updatable, drawable
    
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill('black')

        for thing in updatable:
            thing.update(dt)
        for asteriod in asteroidable:
            if player.collides_with(asteriod):
                print("Game Over!")
                return

        for thing in drawable:
            thing.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60) / 1000    

if __name__ == "__main__":
    main()
