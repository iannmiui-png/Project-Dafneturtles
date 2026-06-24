from turtle import *

A = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0"

M = [
    [0,4,8,3,7],
    [4,8,3,4,5],
    [8,3,7,5,3],
    [3,4,5,3,1],
    [7,5,3,1,0],
]

DAFNE0 = [
    "DAFNE",
    "ABRDN",
    "FR0RF",
    "NDRBA",
    "ENFAD",
]

def add1_cell(ch):
    idx = A.index(ch)
    return A[(idx + 1) % len(A)]

def mul5x5_cell(ch, off):
    idx = A.index(ch)
    return A[(idx + off) % len(A)]

# 9 zones (3x3) mapped onto 5x5
ZONES = [
    [(0,0),(0,1),(1,0),(1,1)],
    [(0,2),(0,3),(1,2),(1,3)],
    [(0,4),(1,4)],
    [(2,0),(2,1),(3,0),(3,1)],
    [(2,2),(2,3),(3,2),(3,3)],
    [(2,4),(3,4)],
    [(4,0),(4,1)],
    [(4,2),(4,3)],
    [(4,4)],
]

CELL = 10

# 14-step pink->yellow->brown->green palette
PALETTE14 = [
    (1.00, 0.40, 0.70),
    (1.00, 0.50, 0.65),
    (1.00, 0.60, 0.55),
    (1.00, 0.70, 0.40),
    (1.00, 0.80, 0.20),
    (1.00, 0.90, 0.00),
    (0.90, 0.75, 0.00),
    (0.70, 0.55, 0.10),
    (0.55, 0.55, 0.05),
    (0.40, 0.55, 0.10),
    (0.30, 0.70, 0.00),
    (0.20, 0.80, 0.00),
    (0.10, 0.85, 0.05),
    (0.00, 0.90, 0.10),
]

def color14_for_letter(ch):
    return PALETTE14[A.index(ch) % 14]

def main():
    screen = Screen()
    screen.tracer(0, 0)
    colormode(1.0)

    block_t = Turtle(visible=False)
    text_t  = Turtle(visible=False)

    for t in (block_t, text_t):
        t.speed(0)
        t.up()
        t.hideturtle()

    def draw_cell(r, c, ch, x0, y0):
        # keep original "generally represents the shade" behavior
        shade = ord(ch) / 255.0
        block_t.color(shade, shade, shade)
        block_t.up()
        block_t.goto(x0 + c*CELL, y0 - r*CELL)
        block_t.down()
        block_t.begin_fill()
        for _ in range(4):
            block_t.forward(CELL)
            block_t.right(90)
        block_t.end_fill()
        block_t.up()

    def draw_char(r, c, ch, x0, y0):
        cx = x0 + c*CELL + CELL/2.0
        cy = y0 - r*CELL - CELL/2.0
        rcol, gcol, bcol = color14_for_letter(ch)
        text_t.color(rcol, gcol, bcol)
        text_t.up()
        text_t.goto(cx, cy - 3)
        text_t.write(ch, align="center", font=("Arial", 6, "bold"))

    def draw_full_block(block, x0, y0):
        for r in range(5):
            for c in range(5):
                ch = block[r][c]
                draw_cell(r, c, ch, x0, y0)
                draw_char(r, c, ch, x0, y0)

    x = 0
    y = 0
    b = [list(row) for row in DAFNE0]
    zone = 0

    # initial draw
    draw_full_block(b, x, y)
    screen.update()

    while True:
        # mutate only the active zone
        for (r, c) in ZONES[zone]:
            off = M[r][c]
            if off == 0:
                # ensure corners and any zero-offset cells still move
                b[r][c] = add1_cell(b[r][c])
            else:
                b[r][c] = mul5x5_cell(b[r][c], off)

        # chunky incremental: redraw only mutated cells
        for (r, c) in ZONES[zone]:
            ch = b[r][c]
            draw_cell(r, c, ch, x, y)
            draw_char(r, c, ch, x, y)

        screen.update()
        zone = (zone + 1) % 9

if __name__ == "__main__":
    main()
    mainloop()

