

function drawRoom(s, x, y){
  line(x-s, y-s, x-s, y+s) // left
  line(x+s, y-s, x+s, y+s) // right
  line(x-s, y+s, x+s, y+s) // up
  line(x-s, y-s, x+s, y-s) // down
  text('0', x, y)
}

function setup() {
    drawRoom(1000, 1000);
}

function draw() {
}