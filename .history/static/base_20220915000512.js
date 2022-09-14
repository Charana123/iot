let s = 100;

function setup() {
    createCanvas(1000, 1000);
}


function drawRoom(x, y){
    line(x-s, y-s, x-s, y+s) // left
    line(x+s, y-s, x+s, y+s) // right
    line(x-s, y+s, x+s, y+s) // up
    line(x-s, y-s, x+s, y-s) // down
    text('0', x, y)
}

function draw() {
  ellipse(x, height/2, 20, 20);
  x = x + 1;
}