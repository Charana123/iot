function drawRoom(s, x, y){
  line(x-s, y-s, x-s, y+s) // left
  line(x+s, y-s, x+s, y+s) // right
  line(x-s, y+s, x+s, y+s) // up
  line(x-s, y-s, x+s, y-s) // down
  text('0', x, y)
}

rooms = JSON.parse(document.currentScript.getAttribute('data'));

function setup() {
  createCanvas(3000, 3000);

  rooms.forEach(function (item, index) {
    drawRoom
  });
}