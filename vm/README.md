<pre>A = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0"

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

# 9 zones (3Ã—3) mapped onto 5Ã—5
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

    
CLASS Cell {constructor(a){this.collapsed=!1,this.options=a instanceof Array?a:Array.from({length:a},(_,i)=>i)}}
CLASS Tile {WFC}

  const pgmArrays = [
    [[0,0,0],[0,0,0],[0,0,0]],
    [[3,3,3],[3,3,3],[3,3,3]],
    [[3,3,3],[3,1,0],[3,3,3]],
    [[3,3,3],[1,1,1],[3,3,3]],
    [[0,3,3],[0,1,0],[0,3,3]],
    [[0,3,3],[3,3,3],[3,3,3]],
    [[3,3,3],[0,0,0],[3,3,3]],
    [[3,1,3],[0,1,0],[3,1,3]],
    [[3,1,3],[3,1,3],[3,0,3]],
    [[3,0,3],[0,0,0],[3,3,3]],
    [[3,0,3],[0,3,0],[3,0,3]],
    [[3,0,3],[3,3,0],[3,3,3]],
    [[3,3,3],[0,1,0],[3,3,3]],
  ];
  tiles[0] = new Tile(tileImages[0], ["AAA","AAA","AAA","AAA"]);
  tiles[1] = new Tile(tileImages[1], ["BBB","BBB","BBB","BBB"]);
  tiles[2] = new Tile(tileImages[2], ["BBB","BCB","BBB","BBB"]);
  tiles[3] = new Tile(tileImages[3], ["BBB","BDB","BBB","BDB"]);
  tiles[4] = new Tile(tileImages[4], ["ABB","BCB","BBA","AAA"]);
  tiles[5] = new Tile(tileImages[5], ["ABB","BBB","BBB","BBA"]);
  tiles[6] = new Tile(tileImages[6], ["BBB","BCB","BBB","BCB"]);
  tiles[7] = new Tile(tileImages[7], ["BDB","BCB","BDB","BCB"]);
  tiles[8] = new Tile(tileImages[8], ["BDB","BBB","BCB","BBB"]);
  tiles[9] = new Tile(tileImages[9], ["BCB","BCB","BBB","BCB"]);
  tiles[10] = new Tile(tileImages[10], ["BCB","BCB","BCB","BCB"]);
  tiles[11] = new Tile(tileImages[11], ["BCB","BCB","BBB","BBB"]);
  tiles[12] = new Tile(tileImages[12], ["BBB","BCB","BBB","BCB"]);
  </pre>
