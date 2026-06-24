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
