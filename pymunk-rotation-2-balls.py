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

upper_ball = pymunk.Body()
upper_ball.position = (100, 30)
shape = pymunk.Circle(upper_ball, 15, (0, 0))
shape.mass = 1
shape.elasticity = 0.1
shape.friction = 1
space.add(upper_ball, shape)

lower_ball = pymunk.Body()
lower_ball.position = (400, 470)
shape = pymunk.Circle(lower_ball, 15, (0, 0))
shape.mass = 1
shape.elasticity = 0.1
shape.friction = 1
space.add(lower_ball, shape)

box = pymunk.Body()
box.position = (250, 250)
shape = pymunk.Poly.create_box(box, (300, 30))
shape.mass = 1
shape.elasticity = 0.1
shape.friction = 1
space.add(box, shape)

running = True
active = False
paused = False
active_ball = upper_ball
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if active:
                if event.key == pygame.K_SPACE:
                    upper_ball.position = (100, 30)
                    lower_ball.position = (400, 470)
                    box.position = (250, 250)
                    for body in [upper_ball, lower_ball, box]:
                        body.velocity = (0, 0)
                        body.angular_velocity = 0
                        body.angle = 0
                    active = False
                    paused = False
                    active_ball = upper_ball
                elif event.key == pygame.K_p:
                    paused = not paused
            else:
                if event.key == pygame.K_DOWN:
                    active_ball = lower_ball
                elif event.key == pygame.K_UP:
                    active_ball = upper_ball
                elif event.key == pygame.K_LEFT:
                    active_ball.position += (-10, 0)
                elif event.key == pygame.K_RIGHT:
                    active_ball.position += (10, 0)
                elif event.key == pygame.K_SPACE:
                    upper_ball.apply_impulse_at_local_point((0, 100), (0, 0))
                    lower_ball.apply_impulse_at_local_point((0, -100), (0, 0))
                    active = True

    if active and not paused:
        print(f"pos:{box.position}, v:{box.velocity}")
    if not paused:
        space.step(1 / FPS)
    screen.fill((0, 0, 0))
    space.debug_draw(draw_options)
    pygame.display.flip()
    clock.tick(FPS)
