

function drawRoom(s, x, y){
  console.log(s, x, y)
  line(x-s, y-s, x-s, y+s) // left
  //line(x+s, y-s, x+s, y+s) // right
  //line(x-s, y+s, x+s, y+s) // up
  //line(x-s, y-s, x+s, y-s) // down
  //text('0', x, y)
  //console.log('here')
}

function setup() {
  // line(15, 25, 70, 90);
  createCanvas(1000, 1000);
  drawRoom(5, 50, 50);
}

function draw() {
  // drawRoom(100, 300, 300);
}