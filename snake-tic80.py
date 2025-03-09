# title:   simple snake
# script:  python

import random

snake = [
    {'xc': 14, 'yc': 8},
    {'xc': 15, 'yc': 8},
    {'xc': 16, 'yc': 8},
]
new = {'xc': random.randint(5, 25), 'yc': random.randint(2, 6)}

UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3

speed = 4 # cells/s
direction = RIGHT
dist = 0
def TIC():
    global snake, new, speed, direction, dist

    if btnp(0):
        direction = UP
    elif btnp(1):
        direction = DOWN
    elif btnp(2):
        direction = LEFT
    elif btnp(3):
        direction = RIGHT

    dist += speed * 1/60
    if dist >= 1:
        dist -= 1
        for i in range(len(snake) - 1):
            cell = snake[i]
            nxt = snake[i + 1]
            cell['xc'] = nxt['xc']
            cell['yc'] = nxt['yc']

        head = snake[-1]
        if direction == RIGHT:
            head['xc'] += 1
        elif direction == LEFT:
            head['xc'] -= 1
        elif direction == UP:
            head['yc'] -= 1
        elif direction == DOWN:
            head['yc'] += 1

        if head['xc'] > 29:
            head['xc'] = 0
        elif head['xc'] < 0:
            head['xc'] = 29
        elif head['yc'] > 16:
            head['yc'] = 0
        elif head['yc'] < 0:
            head['yc'] = 16

        for i in range(len(snake) - 1):
            if head == snake[i]:
                speed = 0

        if head == new:
            speed *= 1.1
            snake.insert(0, new)
            new_is_too_near = True
            while new_is_too_near:
                new = {'xc': random.randint(0, 29), 'yc': random.randint(0, 16)}
                new_is_too_near = False
                for cell in snake:
                    dist_x = abs(cell['xc'] - new['xc'])
                    dist_y = abs(cell['yc'] - new['yc'])
                    if dist_x <= 2 and dist_y <= 2:
                        new_is_too_near = True
                        break

    cls(1)
    spr(1, new['xc'] * 8, new['yc'] * 8)
    for cell in snake:
        spr(0, cell['xc'] * 8, cell['yc'] * 8)

# <TILES>
# 000:4444444442222224422222244222222442222224422222244222222444444444
# 001:aaaaaaaaa555555aa555555aa555555aa555555aa555555aa555555aaaaaaaaa
# </TILES>

# <WAVES>
# 000:00000000ffffffff00000000ffffffff
# 001:0123456789abcdeffedcba9876543210
# 002:0123456789abcdef0123456789abcdef
# </WAVES>

# <SFX>
# 000:000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000304000000000
# </SFX>

# <TRACKS>
# 000:100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
# </TRACKS>

# <PALETTE>
# 000:1a1c2c5d275db13e53ef7d57ffcd75a7f07038b76425717929366f3b5dc941a6f673eff7f4f4f494b0c2566c86333c57
# </PALETTE>

