#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if ((w > 0) && (h > 0)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let rect = '';
    let h, w;
    for (let i = 0; i < h; i++) {
      for (let j = 0; j < w; j++) {
        rect += 'X';
      }
      rect += '\n';
    }
    console.log(rect);
  }

  rotate () {
    const aux = this.width;
    this.width = this.height;
    this.height = aux;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
