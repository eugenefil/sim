import pygame
import pymunk
import pymunk.pygame_util

FPS = 60

pygame.init()
screen = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()

space = pymunk.Space()
space.gravity = (0, 1000)
draw_options = pymunk.pygame_util.DrawOptions(screen)

# lines
lines = [
    pymunk.Segment(space.static_body, (40, 300), (400, 350), 0),
    pymunk.Segment(space.static_body, (400, 350), (450, 350), 0),
]
for line in lines:
    line.elasticity = 0.9
    line.friction = 1
space.add(*lines)

# ball
body = pymunk.Body()
body.position = (50, 50)
shape = pymunk.Circle(body, 20, (0, 0))
shape.mass = 50
shape.elasticity = 0.9
shape.friction = 1
space.add(body, shape)

# lower box
body = pymunk.Body()
body.position = (420, 310)
shape = pymunk.Poly.create_box(body, (40, 40))
shape.mass = 1
shape.elasticity = 0.6 # make boxes less bouncy than the ball
shape.friction = 1
space.add(body, shape)

# upper box
body = pymunk.Body()
body.position = (415, 210)
shape = pymunk.Poly.create_box(body, (40, 40))
shape.mass = 1
shape.elasticity = 0.6
shape.friction = 1
space.add(body, shape)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    space.step(1 / FPS)
    screen.fill((0, 0, 0))
    space.debug_draw(draw_options)
    pygame.display.flip()
    clock.tick(FPS)
