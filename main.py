import pygame
from constants import *
from player import *
from circleshape import *
from asteroids import *
from AsteroidField import *
import sys
import random

def main ():
    pygame.init()
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    clock = pygame.time.Clock()
    dt = 0

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Player.containers = (updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0), rect=None)

        for sprite in updatable:
            sprite.update(dt)

        for asteroid in asteroids:
            if asteroid.collision_check(player) == True:
                sys.exit("Game over!")
            for shot in shots:
                if asteroid.collision_check(shot) == True:
                    asteroid.split()
                    shot.kill()
            
            

        for sprite in drawable:   
            sprite.draw(screen)  # Use your custom draw method

        pygame.display.flip()
        dt = clock.tick(60) / 1000



if __name__ == "__main__":
    main()