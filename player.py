from constants import *
from circleshape import *

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.x = x
        self.y = y
        self.rotation = 0
    
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    #Keybindings
    def update(self, dt):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:    #key a -> turn left
            self.rotate(-dt)
        if keys[pygame.K_d]:    #key d -> turn right
            self.rotate(dt)
        if keys[pygame.K_w]:    #key w -> move up
            self.move(dt)
        if keys[pygame.K_s]:    #key s -> move down
            self.move(-dt)
        if keys[pygame.K_SPACE]:#key SPACE -> shoot bullet
            self.shoot()
    
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, (255, 255, 255), (self.triangle()), 2) #rgb, shape and line width

    def shoot(self):
        bullet = Shot(self.position.x, self.position.y, SHOT_RADIUS)
        bullet.velocity = pygame.Vector2(0, 1)
        bullet.velocity = bullet.velocity.rotate(self.rotation)
        bullet.velocity *= PLAYER_SHOOT_SPEED
    
class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, SHOT_RADIUS, 2)
    
    def update(self, dt):
        self.position += self.velocity * dt