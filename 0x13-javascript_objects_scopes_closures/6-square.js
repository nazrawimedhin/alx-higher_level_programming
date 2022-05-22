#!/usr/bin/node
const square5 = require('./5-square');

class Square extends square5 {
  charprint (c) {
    if (c === undefined) {
      c = 'X';
    }
    let square = '';
    for (let i = 0; i < c; i++) {
      let j;
      for (j = 0; j < c; j++) {
        square += c;
      }
      square += '\n';
    }
    console.log(square);
  }
}
