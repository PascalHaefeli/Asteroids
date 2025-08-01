import pygame
from constants import *
from circleshape import *
from player import *
from asteroid import *
from asteroidfield import *

def main():
    #startup
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.get_init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    #group declarations
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    #group assignments
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    #spawn objects
    PC = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    print(f"updatable: {updatable}")
    print(f"drawable: {drawable}")

    #GameLoop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0, 0, 0))
        updatable.update(dt)
        for asteroid in asteroids:
            if asteroid.collider(PC):
                print("Game Over!")
                pygame.QUIT
                return
        for object in drawable:
            object.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000

#keeps main() from being executed when imported by other modules; only executes if main.py is run
if __name__ == "__main__":
    main()