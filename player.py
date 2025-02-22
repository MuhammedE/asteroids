from circleshape import *
from constants import *
from shot import *

class Player(CircleShape):
    containers = None
    def __init__(self,x,y):
        super().__init__(x,y,PLAYER_RADIUS)
        self.rotation = 0
        self.time_until_shooting_possible = 0
    
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    def rotate(self,dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self,dt):
        forward = pygame.Vector2(0,1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt    

    def shoot(self):
        
        if self.time_until_shooting_possible <= 0:
            print(f"self.position.x = {self.position.x}, self.position.y = {self.position.y}")
            shot = Shot(self.position.x,self.position.y)
            shot.velocity = pygame.Vector2(0,1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
            self.time_until_shooting_possible = PLAYER_SHOOT_COOLDOWN 

    def draw(self,screen):
        white = pygame.Color(255,255,255)
        pygame.draw.polygon(screen,white,self.triangle(),2)

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_SPACE]:
            self.shoot()
        
        if self.time_until_shooting_possible > 0:
            self.time_until_shooting_possible -= dt