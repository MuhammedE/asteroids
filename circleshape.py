import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen:pygame.Surface) -> None:
        # sub-classes must override
        pass

    def update(self, dt: float) -> None:
        # sub-classes must override
        pass

    def is_colliding(self,other_circle: "CircleShape") -> bool:
        distance = self.position.distance_to(other_circle.position)
        sum_radius = self.radius + other_circle.radius
        if distance <= sum_radius:
            return True
        else:
            return False