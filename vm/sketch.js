const tiles = [];
const tileImages = [];
let grid = [];

const DIM = 17;

function createImageFromArray(array) {
  const w = array[0].length;
  const h = array.length;
  const buf = createGraphics(w, h);
  buf.pixelDensity(1);
  buf.loadPixels();

  for (let y = 0; y < h; y++) {
    for (let x = 0; x < w; x++) {
      const v = array[y][x];
      const g = map(v, 0, 3, 0, 255);
      let col = (g === 0) ? color(0, 0, 0, 0) : color(255);
      buf.set(x, y, col);
    }
  }

  buf.updatePixels();
  return buf.get();
}

function preload() {
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

  for (let i = 0; i < pgmArrays.length; i++) {
    tileImages[i] = createImageFromArray(pgmArrays[i]);
  }
}

function setup() {
  fxpreview();
  createCanvas(innerWidth, innerHeight);

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

  for (let i = 2; i < 14; i++) {
    for (let r = 1; r < 4; r++) {
      tiles.push(tiles[i].rotate(r));
    }
  }

  for (let t of tiles) t.analyze(tiles);

  startOver();
}

function startOver() {
  grid = [];
  for (let i = 0; i < DIM * DIM; i++) {
    grid[i] = new Cell(tiles.length);
  }
}

function checkValid(arr, valid) {
  for (let i = arr.length - 1; i >= 0; i--) {
    if (!valid.includes(arr[i])) arr.splice(i, 1);
  }
}

function draw() {
  background(0);

  const w = width / DIM;
  const h = height / DIM;

  for (let j = 0; j < DIM; j++) {
    for (let i = 0; i < DIM; i++) {
      const cell = grid[i + j * DIM];
      if (cell.collapsed) {
        image(tiles[cell.options[0]].img, i * w, j * h, w, h);
      } else {
        noFill();
        stroke(40);
        rect(i * w, j * h, w, h);
      }
    }
  }

  let candidates = grid.filter(c => !c.collapsed);
  if (candidates.length === 0) return;

  candidates.sort((a, b) => a.options.length - b.options.length);
  const minEntropy = candidates[0].options.length;
  candidates = candidates.filter(c => c.options.length === minEntropy);

  const cell = random(candidates);
  cell.collapsed = true;
  const pick = random(cell.options);
  if (pick === undefined) {
    startOver();
    return;
  }
  cell.options = [pick];

  const next = [];

  for (let j = 0; j < DIM; j++) {
    for (let i = 0; i < DIM; i++) {
      const idx = i + j * DIM;
      const c = grid[idx];

      if (c.collapsed) {
        next[idx] = c;
        continue;
      }

      let opts = [...Array(tiles.length).keys()];

      if (j > 0) {
        let up = grid[i + (j - 1) * DIM];
        let valid = [];
        for (let o of up.options) valid.push(...tiles[o].down);
        checkValid(opts, valid);
      }

      if (i < DIM - 1) {
        let right = grid[i + 1 + j * DIM];
        let valid = [];
        for (let o of right.options) valid.push(...tiles[o].left);
        checkValid(opts, valid);
      }

      if (j < DIM - 1) {
        let down = grid[i + (j + 1) * DIM];
        let valid = [];
        for (let o of down.options) valid.push(...tiles[o].up);
        checkValid(opts, valid);
      }

      if (i > 0) {
        let left = grid[i - 1 + j * DIM];
        let valid = [];
        for (let o of left.options) valid.push(...tiles[o].right);
        checkValid(opts, valid);
      }

      next[idx] = new Cell(opts);
    }
  }

  grid = next;
}
