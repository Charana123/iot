function setup() {
    createCanvas(3000, 3000);
    drawRoom(100, 300, 300);
    drawRoom(100, 800, 800);
    drawRoom(100, 300, 800);
    drawRoom(100, 800, 300);
}

data = JSON.parse(document.currentScript.getAttribute('data'));
console.log(data)