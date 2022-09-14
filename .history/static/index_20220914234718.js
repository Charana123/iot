let x = 0;

function setup() {
    createCanvas(600, 400);
    line(15, 25, 70, 90);
}

function draw() {
  ellipse(x, height/2, 20, 20);
  x = x + 1;
}