import pygame

H = W = 500
K = 10
G = 10
R = 50
M = 1
PIXELS_PER_METER = 200

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode([W, H])

v0 = 0.0
a = 0.0
y = 0.0

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    dt = clock.tick(60) / 1000;
    y += v0 * dt + a * dt**2 / 2
    print(f'dt:{dt:.3f} v0:{v0:.3f} a:{a:.3f} y:{y:.3f}')
    v = v0 + a * dt
    v0 = v
    f = M * G - K * y
    a = f / M

    screen.fill((0, 0, 0))
    pygame.draw.circle(screen, (255, 0, 0), (W // 2, y * PIXELS_PER_METER + R), R)
    pygame.display.flip()

pygame.quit()
