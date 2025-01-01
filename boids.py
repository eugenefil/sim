import pygame
import random

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
MARGIN = 50
PROTECTED_RANGE = 10
VISIBLE_RANGE = 50
N = 50
VX_MAX = 20
VY_MAX = 20
AVOID_FACT = 0.5
TURN_FACT = 2
CENTER_FACT = 0.01
MATCH_FACT = 0.5

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

boids = []
for _ in range(N):
    boids.append({
        'x': random.randint(0, SCREEN_WIDTH),
        'y': random.randint(0, SCREEN_HEIGHT),
        'vx': random.randint(-VX_MAX, VX_MAX),
        'vy': random.randint(-VY_MAX, VY_MAX),
    })

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 0))
    for i in range(len(boids)):
        boid = boids[i]
        neighbors = 0
        neighbor_x_avg = 0
        neighbor_y_avg = 0
        neighbor_vx_avg = 0
        neighbor_vy_avg = 0
        for j in range(len(boids)):
            if i == j:
                continue
            other = boids[j]
            dist_x = boid['x'] - other['x']
            dist_y = boid['y'] - other['y']
            if abs(dist_x) < PROTECTED_RANGE and abs(dist_y) < PROTECTED_RANGE:
                boid['vx'] += dist_x * AVOID_FACT
                boid['vy'] += dist_y * AVOID_FACT
            elif abs(dist_x) < VISIBLE_RANGE and abs(dist_y) < VISIBLE_RANGE:
                neighbors += 1
                neighbor_x_avg += other['x']
                neighbor_y_avg += other['y']
                neighbor_vx_avg += other['vx']
                neighbor_vy_avg += other['vy']

        if neighbors > 0:
            neighbor_x_avg /= neighbors
            neighbor_y_avg /= neighbors
            boid['vx'] += (neighbor_x_avg - boid['x']) * CENTER_FACT
            boid['vy'] += (neighbor_y_avg - boid['y']) * CENTER_FACT

            neighbor_vx_avg /= neighbors
            neighbor_vy_avg /= neighbors
            boid['vx'] += (neighbor_vx_avg - boid['vx']) * MATCH_FACT
            boid['vy'] += (neighbor_vy_avg - boid['vy']) * MATCH_FACT

        if boid['x'] > SCREEN_WIDTH - MARGIN:
            boid['vx'] -= TURN_FACT
        if boid['x'] < MARGIN:
            boid['vx'] += TURN_FACT
        if boid['y'] > SCREEN_HEIGHT - MARGIN:
            boid['vy'] -= TURN_FACT
        if boid['y'] < MARGIN:
            boid['vy'] += TURN_FACT

        if boid['vx'] > VX_MAX:
            boid['vx'] = VX_MAX
        if boid['vx'] < -VX_MAX:
            boid['vx'] = -VX_MAX
        if boid['vy'] > VY_MAX:
            boid['vy'] = VY_MAX
        if boid['vy'] < -VY_MAX:
            boid['vy'] = -VY_MAX

        boid['x'] += boid['vx']
        boid['y'] += boid['vy']
        pygame.draw.circle(screen, (255, 0, 0), (boid['x'], boid['y']), 5)

    pygame.display.flip()
    clock.tick(60)
