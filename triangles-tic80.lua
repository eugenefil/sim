-- script:  lua

-- original at https://github.com/nesbox/TIC-80/wiki/tri

function TIC()
    cls()
    t = time() / 1000
    for y = 1, 136, 27 do
        for x = 0, 240, 27 do
            a = t / 50 * (x + y + 100)
            dx = 12 * math.sin(a)
            dy = 12 * math.cos(a)
            xtop = x + 12 + dx
            ytop = y + 12 - dy
            xright = x + 25
            ybot = y + 25
            tri(x, y, xtop, ytop, xright, y, 1) -- top triangle
            tri(xright, y, xtop, ytop, xright, ybot, 2) -- right triangle
            tri(xright, ybot, xtop, ytop, x, ybot, 3) -- bottom triangle
            tri(x, ybot, xtop, ytop, x, y, 4) -- left triangle
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

