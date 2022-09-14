let x = 100;

function setup() {
    createCanvas(600, 400);
    line(15, 25, 70, 90);
}


function drawRoom(x, y){
    line(x+100)
}

function draw() {
  ellipse(x, height/2, 20, 20);
  x = x + 1;
}