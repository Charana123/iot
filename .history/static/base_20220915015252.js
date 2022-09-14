function drawRoom(s, x, y, count){
  line(x-s, y-s, x-s, y+s) // left
  line(x+s, y-s, x+s, y+s) // right
  line(x-s, y+s, x+s, y+s) // up
  line(x-s, y-s, x+s, y-s) // down
  text(count, x, y)
}

rooms = JSON.parse(document.currentScript.getAttribute('data'));

function setup() {
  createCanvas(3000, 3000);
  textSize(32);

  rooms.forEach(function (room) {
    drawRoom(100, room['x'], room['y'], room['count'])
  });
}