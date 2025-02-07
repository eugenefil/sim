import pygame
import random

pygame.init()
screen = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()
pygame.key.set_repeat(50)

RIGHT = 1
LEFT = -1
UP = 2
DOWN = -2

snake = [
    {'xc': 24, 'yc': 25},
    {'xc': 25, 'yc': 25},
    {'xc': 26, 'yc': 25},
]
newcell = {'xc': random.randint(5, 45), 'yc': random.randint(5, 20)}

speed = 8
dist = 0
direction = RIGHT
running = True
gameover = False
while running:
    speedup = 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            newdir = None
            if event.key == pygame.K_RIGHT:
                newdir = RIGHT
            elif event.key == pygame.K_LEFT:
                newdir = LEFT
            elif event.key == pygame.K_UP:
                newdir = UP
            elif event.key == pygame.K_DOWN:
                newdir = DOWN

            if newdir is not None:
                if newdir != direction:
                    if newdir != -direction:
                        direction = newdir
                else:
                    speedup = 4

    t = clock.tick(60) / 1000
    dist += speedup * speed * t
    if dist > 1 and not gameover:
        dist -= 1
        for i in range(len(snake) - 1):
            cell = snake[i]
            nextcell = snake[i + 1]
            cell['xc'] = nextcell['xc']
            cell['yc'] = nextcell['yc']

        head = snake[-1]
        if direction == RIGHT:
            head['xc'] += 1
        elif direction == LEFT:
            head['xc'] -= 1
        elif direction == UP:
            head['yc'] -= 1
        elif direction == DOWN:
            head['yc'] += 1

        if head['xc'] > 49:
            head['xc'] = 0
        if head['xc'] < 0:
            head['xc'] = 49
        if head['yc'] > 49:
            head['yc'] = 0
        if head['yc'] < 0:
            head['yc'] = 49

        for j in range(len(snake) - 1):
            cell = snake[j]
            if head['xc'] == cell['xc'] and head['yc'] == cell['yc']:
                gameover = True
                break

        if head['xc'] == newcell['xc'] and head['yc'] == newcell['yc']:
            snake.insert(0, snake[0].copy())
            speed *= 1.05
            while True:
                newcell = {'xc': random.randint(0, 49), 'yc': random.randint(0, 49)}
                badcell = False
                for cell in snake:
                    dist_x = cell['xc'] - newcell['xc']
                    dist_y = cell['yc'] - newcell['yc']
                    if abs(dist_x) < 3 and abs(dist_y) < 3:
                        badcell = True
                        break
                if not badcell:
                    break

    screen.fill((0, 0, 0))
    x = newcell['xc'] * 10
    y = newcell['yc'] * 10
    pygame.draw.rect(screen, (255, 0, 255), pygame.Rect(x, y, 10, 10))
    for i, cell in enumerate(reversed(snake)):
        color = (255, 0, 0) if i % 2 == 0 else (0, 255, 0)
        x = cell['xc'] * 10
        y = cell['yc'] * 10
        pygame.draw.rect(screen, color, pygame.Rect(x, y, 10, 10))

    pygame.display.flip()
