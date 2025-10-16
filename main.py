import pygame
from constants import *
from player import *

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawwable = pygame.sprite.Group()
    Player.containers = updatable, drawwable
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill('black')

        for thing in updatable:
            thing.update(dt)
        for thing in drawwable:
            thing.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60) / 1000    
        
if __name__ == "__main__":
    main()
