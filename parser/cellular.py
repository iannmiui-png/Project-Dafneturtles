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

# 9 zones (3×3) mapped onto 5×5
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

def draw_cell(x, y, letter):
    shade = ord(letter) / 255
    color(shade, shade, shade)
    up()
    goto(x, y)
    down()
    begin_fill()
    for _ in range(4):
        forward(CELL)
        right(90)
    end_fill()

def draw_block(block, x, y):
    for r in range(5):
        for c in range(5):
            draw_cell(x + c*CELL, y - r*CELL, block[r][c])

def main():
    speed(0)
    colormode(1.0)
    ht()
    tracer(0,0)

    x = 0
    y = 0

    b = [list(row) for row in DAFNE0]
    zone = 0

    while True:
        # mutate only the current zone
        for (r,c) in ZONES[zone]:
            b[r][c] = mul5x5_cell(b[r][c], M[r][c])

        clear()
        draw_block(["".join(r) for r in b], x, y)
        update()

        zone = (zone + 1) % 9

if __name__ == "__main__":
    main()
    mainloop()
