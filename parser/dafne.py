from turtle import *

################################
# DAFNE core
################################

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

def add1(block):
    out = []
    for i in range(5):
        row = ""
        for j in range(5):
            idx = A.index(block[i][j])
            row += A[(idx + 1) % len(A)]
        out.append(row)
    return out

def mul5x5(block):
    out = []
    for i in range(5):
        row = ""
        for j in range(5):
            idx = A.index(block[i][j])
            off = M[i][j]
            row += A[(idx + off) % len(A)]
        out.append(row)
    return out

################################
# DRAWING UTILITIES (COMPACT)
################################

CELL = 10   # *** SMALLER CELLS ***
FONT = ("Times New Roman", 6, "normal")  # *** SMALLER FONT ***

def draw_cell(x, y, letter):
    shade = ord(letter) / 255

    # Draw filled square
    color(shade, shade, shade)
    up()
    goto(x, y)
    down()
    begin_fill()
    for _ in range(4):
        forward(CELL)
        right(90)
    end_fill()

    # Pink letter
    up()
    goto(x + CELL/2, y - CELL + 2)
    color(1, 0.4, 0.7)
    write(letter, align="center", font=FONT)

def draw_block(block, x, y):
    for r in range(5):
        for c in range(5):
            draw_cell(x + c*CELL, y - r*CELL, block[r][c])

################################
# MAIN LAYOUT (COMPACT)
################################

def main():
    speed(0)
    colormode(1.0)
    ht()

    # Generate all 28 states
    states = []
    b = DAFNE0
    states.append(b)
    b = add1(b)
    states.append(b)
    for _ in range(26):
        b = mul5x5(b)
        states.append(b)

    # Start at (0,0) for compact layout
    x = -50
    y = 150

    # Draw states 0â€“15 downward
    for i in range(16):
        draw_block(states[i], x, y)
        y -= CELL*5 + 4   # compact spacing

    # Base for branching
    base_x = x
    base_y = y + CELL*5 + 4

    # Even states â†’ right
    ex = base_x + CELL*5 + 20
    ey = base_y
    for s in [16,18,20,22,24,26,28]:
        draw_block(states[s], ex, ey)
        ey -= CELL*5 + 4

    # Odd states â†’ left
    ox = base_x - CELL*5 - 20
    oy = base_y
    for s in [17,19,21,23,25,27]:
        draw_block(states[s], ox, oy)
        oy -= CELL*5 + 4

    return "Done!"

if __name__ == "__main__":
    print(main())
    mainloop()

