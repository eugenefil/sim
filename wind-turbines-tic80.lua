-- script:  lua

turbines = {}
dx = 0
for y = 66, 135, 33 do
    for x = 10, 220, 45 do
        w = 3 + y / 20 -- the lower to screen bottom the bigger the turbine
        table.insert(turbines, {
            x = x + dx,
            y = y,
            w = w,
            h = w * 7,
            r = w * 3,
            da = math.random() * math.pi,
        })
    end
    dx = dx + 15
end

speed = 2
rot = 0

function TIC()
    if btnp(0) then speed = speed + 1 end
    if btnp(1) then speed = speed - 1 end
    if speed < -10 then speed = -10 end
    if speed > 10 then speed = 10 end
    if math.abs(speed) > 7 then
        max_offset = math.abs(speed) - 6
        poke(0x3ffa, (math.random() * 2 - 1) * max_offset) -- earth shaking
    else
        poke(0x3ffa, 0)
    end

    dt = 1 / 60
    rot = rot + dt * math.pi / 3 * speed

    cls(6) -- grass
    rect(0, 0, 240, 60, 9) -- sky
    for _, t in ipairs(turbines) do
        -- body
        xc = t.x + t.w / 2
        yc = t.y - t.h
        tri(t.x, t.y, xc, yc, t.x + t.w, t.y, 12)
        line(xc, yc, xc, yc + 5, 12)

        -- blades
        for a = 0, 2 * math.pi, 2 * math.pi / 3 do
            xe = xc + t.r * math.cos(rot + a + t.da)
            ye = yc - t.r * math.sin(rot + a + t.da)
            line(xc, yc, xe, ye, 12)
        end
    end
end

-- <TILES>
-- 001:eccccccccc888888caaaaaaaca888888cacccccccacc0ccccacc0ccccacc0ccc
-- 002:ccccceee8888cceeaaaa0cee888a0ceeccca0ccc0cca0c0c0cca0c0c0cca0c0c
-- 003:eccccccccc888888caaaaaaaca888888cacccccccacccccccacc0ccccacc0ccc
-- 004:ccccceee8888cceeaaaa0cee888a0ceeccca0cccccca0c0c0cca0c0c0cca0c0c
-- 017:cacccccccaaaaaaacaaacaaacaaaaccccaaaaaaac8888888cc000cccecccccec
-- 018:ccca00ccaaaa0ccecaaa0ceeaaaa0ceeaaaa0cee8888ccee000cceeecccceeee
-- 019:cacccccccaaaaaaacaaacaaacaaaaccccaaaaaaac8888888cc000cccecccccec
-- 020:ccca00ccaaaa0ccecaaa0ceeaaaa0ceeaaaa0cee8888ccee000cceeecccceeee
-- </TILES>

-- <WAVES>
-- 000:00000000ffffffff00000000ffffffff
-- 001:0123456789abcdeffedcba9876543210
-- 002:0123456789abcdef0123456789abcdef
-- </WAVES>

-- <SFX>
-- 000:000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000304000000000
-- </SFX>

-- <TRACKS>
-- 000:100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
-- </TRACKS>

-- <PALETTE>
-- 000:1a1c2c5d275db13e53ef7d57ffcd75a7f07038b76425717929366f3b5dc941a6f673eff7f4f4f494b0c2566c86333c57
-- </PALETTE>

