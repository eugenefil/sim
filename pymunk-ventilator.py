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

line = pymunk.Segment(space.static_body, (500, 0), (500, 400), 5)
line.elasticity = 0.5
line.friction = 0.1
space.add(line)

line = pymunk.Segment(space.static_body, (500, 400), (100, 450), 5)
line.elasticity = 0.5
line.friction = 0.1
space.add(line)

def make_ball():
    body = pymunk.Body()
    body.position = (400, 50)
    r = random.randint(10, 25)
    shape = pymunk.Circle(body, r)
    shape.mass = r / 10
    shape.elasticity = 0.5
    shape.friction = 0.1
    space.add(body, shape)
    return shape

shapes = []
for _ in range(20):
    shapes.append(make_ball())

while True:
    for i in range(len(shapes)):
        shape = shapes[i]
        body = shape.body
        if body.position.y > 550:
            space.remove(body, shape)
            shapes[i] = make_ball()
        elif body.position.x < 100:
            # when using forces, make sure friction and elasticity
            # do not have high values, otherwise bodies start getting
            # enormous velocities and fly through obstacles
            body.apply_force_at_world_point((0, -2500), (0, 0))
            if body.position.y < 300:
                body.apply_force_at_world_point((300, 0), (0, 0))

    space.step(1/60)
    screen.fill((0, 0, 0))
    space.debug_draw(draw_opts)
    pygame.display.flip()
    clock.tick(60)
