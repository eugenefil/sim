import pygame

W = 500
H = 1000
WATER_HEIGHT = 0.6 * H
G = 10
R = 30
M = 100
DENSITY_AIR = 1
DENSITY_WATER = 1000
DRAG_COEF = 0.47
PIXELS_PER_METER = 50

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
    y_pix = y * PIXELS_PER_METER
    v = v0 + a * dt
    density = DENSITY_WATER if y_pix > WATER_HEIGHT else DENSITY_AIR
    f_drag = 0.5 * density * v**2 * DRAG_COEF * (3.14 * (R / PIXELS_PER_METER)**2)
    print(f'dt:{dt:.3f} v0:{v0:.3f} a:{a:.3f} y:{y:.3f} f_drag:{f_drag:.3f}')
    f = M * G - f_drag
    a = f / M
    v0 = v

    screen.fill((0, 0, 0))
    pygame.draw.line(screen, (0, 0, 255), (0, WATER_HEIGHT), (W, WATER_HEIGHT), 1)
    pygame.draw.circle(screen, (255, 0, 0), (W // 2, y_pix), R)
    pygame.display.flip()

pygame.quit()
