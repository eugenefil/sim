import pygame
import pymunk
import pymunk.pygame_util

FPS = 60

pygame.init()
screen = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()
pygame.key.set_repeat(100)

space = pymunk.Space()
space.gravity = (0, 0)
draw_options = pymunk.pygame_util.DrawOptions(screen)

ball = pymunk.Body()
ball.position = (100, 30)
shape = pymunk.Circle(ball, 15, (0, 0))
shape.mass = 1
shape.elasticity = 0.1
shape.friction = 1
space.add(ball, shape)

box = pymunk.Body()
box.position = (250, 250)
shape = pymunk.Poly.create_box(box, (300, 30))
shape.mass = 1
shape.elasticity = 0.1
shape.friction = 1
space.add(box, shape)

running = True
active = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if active:
                if event.key == pygame.K_SPACE:
                    ball.position = (100, 30)
                    ball.velocity = (0, 0)
                    ball.angular_velocity = 0
                    ball.angle = 0
                    box.position = (250, 250)
                    box.velocity = (0, 0)
                    box.angular_velocity = 0
                    box.angle = 0
                    active = False
            else:
                if event.key == pygame.K_LEFT:
                    ball.position += (-10, 0)
                elif event.key == pygame.K_RIGHT:
                    ball.position += (10, 0)
                elif event.key == pygame.K_SPACE:
                    ball.apply_impulse_at_local_point((0, 100), (0, 0))
                    active = True
    if active:
        print(f"pos:{box.position}, v:{box.velocity}")

    space.step(1 / FPS)
    screen.fill((0, 0, 0))
    space.debug_draw(draw_options)
    pygame.display.flip()
    clock.tick(FPS)
