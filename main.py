import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *

def main():
    pygame.init()
    print("Starting Asteroids!")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    clock = pygame.time.Clock()
    dt = 0

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable, )
    Shot.containers = (shots, updatable, drawable)

    player = Player(x, y)
    asteroids_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0, 0, 0))

        dt = clock.tick(60) / 1000

        for entity in updatable:
            entity.update(dt)
        for entity in drawable:
            entity.draw(screen)
        for asteroid in asteroids:
            if player.check_collisons(asteroid):
                print("Game Over!")
                pygame.quit()
                return
            for shot in shots:
                if asteroid.check_collisons(shot):
                    shot.kill()
                    asteroid.split()
        pygame.display.flip()


if __name__ == "__main__":
    main()
