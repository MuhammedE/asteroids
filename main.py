import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    drawables = pygame.sprite.Group()
    updatables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (drawables,updatables)
    Asteroid.containers = (asteroids,drawables,updatables)
    AsteroidField.containers = updatables
    Shot.containers = (shots,drawables,updatables)
    
    

    player = Player(x,y)
    asteroid_field = AsteroidField()
    
    while True:
        if Player.shot_fired == True:
            print("shot fired")
            print(shots)
            print(asteroids)
            Player.shot_fired = False
        for sprite in updatables:
            sprite.update(dt)
        for asteroid in asteroids:
            if asteroid.is_colliding_with(player):
                print("Game Over")
                exit(0)
            
        for asteroid in asteroids:
             for shot in shots:
                if asteroid.is_colliding_with(shot):
                    print("Colliding")
                    asteroid.split()
                    shot.kill()
                    

        
        screen.fill((0,0,0))
        
        for sprite in drawables:
            sprite.draw(screen)
        
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
