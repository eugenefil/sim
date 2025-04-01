# script:  python

# The original snow demo https://tic80.com/play?cart=4179 is shorter and smarter.
# It has no state. Instead, it generates flake's x and y as a function of time().
# It uses sines for swinging. Had to make it more bloated and replace sines with
# horizontal movement and state to make it more approachable for kids.

import random

FLAKES_NUM = 1000
flakes = []
for i in range(FLAKES_NUM):
    swing = random.uniform(3, 10)
    xdir = 1 if random.randint(0, 1) == 1 else -1
    flakes.append({
        'xbase': i * 240 // FLAKES_NUM,
        'y': random.randint(0, 135),
        'swing': swing,
        'dx': random.uniform(-swing, swing),
        'vx': xdir * random.uniform(4, 10),
        'vy': random.uniform(10, 20),
    })

frame = 0
def TIC():
    global flakes, frame

    cls(13)
    dt = 1 / 60

    # draw flakes
    for flake in flakes:
        flake['dx'] += flake['vx'] * dt
        if abs(flake['dx']) >= flake['swing']:
            flake['vx'] = -flake['vx']
        x = flake['xbase'] + flake['dx']

        flake['y'] += flake['vy'] * dt
        if flake['y'] >= 136: # no float modulo in pocketpy
            flake['y'] -= 136
        pix(round(x), round(flake['y']), 12) # TIC error if no rounding

    frame += 1
    if frame % 10 > 0:
        return

    # draw snow on the ground
    vbank(1)
    # choose random point on the ground
    x = random.randint(0, 239)
    y = 135
    # move up to the top of the snow heap
    while y > 0 and pix(x, y) > 0:
        y -= 1
    # draw a triangle on the top - this is how snow heap grows
    tri(x, y, x - 16, y + 8, x + 16, y + 8, 12)
    vbank(0)

# <TILES>
# 001:eccccccccc888888caaaaaaaca888888cacccccccacc0ccccacc0ccccacc0ccc
# 002:ccccceee8888cceeaaaa0cee888a0ceeccca0ccc0cca0c0c0cca0c0c0cca0c0c
# 003:eccccccccc888888caaaaaaaca888888cacccccccacccccccacc0ccccacc0ccc
# 004:ccccceee8888cceeaaaa0cee888a0ceeccca0cccccca0c0c0cca0c0c0cca0c0c
# 017:cacccccccaaaaaaacaaacaaacaaaaccccaaaaaaac8888888cc000cccecccccec
# 018:ccca00ccaaaa0ccecaaa0ceeaaaa0ceeaaaa0cee8888ccee000cceeecccceeee
# 019:cacccccccaaaaaaacaaacaaacaaaaccccaaaaaaac8888888cc000cccecccccec
# 020:ccca00ccaaaa0ccecaaa0ceeaaaa0ceeaaaa0cee8888ccee000cceeecccceeee
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

