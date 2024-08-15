import pygame
import pymunk
import pymunk.pygame_util
import random

pygame.init()
screen = pygame.display.set_mode([500, 500])
clock = pygame.time.Clock()

space = pymunk.Space()
space.gravity = (0, 1000)
draw_opts = pymunk.pygame_util.DrawOptions(screen)

line = pymunk.Segment(space.static_body, (0, 500), (0, 100), 5)
line.elasticity = 0.5
line.friction = 0.1
space.add(line)

line = pymunk.Segment(space.static_body, (0, 100), (200, 0), 5)
line.elasticity = 0.5
line.friction = 0.1
space.add(line)

line = pymunk.Segment(space.static_body, (200, 0), (500, 0), 5)
line.elasticity = 0.5
line.friction = 0.1
space.add(line)

line = pymunk.Segment(space.static_body, (500, 0), (500, 300), 5)
line.elasticity = 0.5
line.friction = 0.1
space.add(line)

line = pymunk.Segment(space.static_body, (500, 300), (100, 350), 5)
line.elasticity = 0.5
line.friction = 0.1
space.add(line)

balls = []
for _ in range(20):
    body = pymunk.Body()
    body.position = (400, 50)
    r = random.randint(10, 20)
    shape = pymunk.Circle(body, r)
    shape.mass = r / 10
    shape.elasticity = 0.5
    shape.friction = 0.1
    space.add(body, shape)
    balls.append(body)

while True:
    for ball in balls:
        if ball.position.y > 550:
            ball.position = (400, 50)
        elif ball.position.x < 100:
            # when using forces, make sure friction and elasticity
            # do not have high values, otherwise bodies start getting
            # enormous velocities and fly through obstacles
            ball.apply_force_at_world_point((0, -2000), (0, 0))
            if ball.position.y < 300:
                ball.apply_force_at_world_point((300, 0), (0, 0))

    space.step(1/60)
    screen.fill((0, 0, 0))
    space.debug_draw(draw_opts)
    pygame.display.flip()
    clock.tick(60)
