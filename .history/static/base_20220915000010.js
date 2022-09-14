let s = 100;

function setup() {
    createCanvas(600, 400);
    line(15, 25, 70, 90);
}


function drawRoom(x, y){
    line(x-s, y-s, x-s, y+s) // left
    line(x+s, y-s, x+s, y+s) // right
    line(x-s, y+s, x+ss, y+s) // up
    line(x-s, y-s, x-s, y+s) // down
}

function draw() {
  ellipse(x, height/2, 20, 20);
  x = x + 1;
}