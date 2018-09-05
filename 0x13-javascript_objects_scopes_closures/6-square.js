#!/usr/bin/node

class Square extends require('./5-square') {
  charPrint (c) {
    if (c === undefined) {
      for (let i = 0; i < this.height; i++) {
        let square = '';
        for (let j = 0; j < this.width; j++) {
          square += 'X';
        }
        console.log(square);
      }
    } else {
      for (let i = 0; i < this.height; i++) {
        let square = '';
        for (let j = 0; j < this.width; j++) {
          square += 'C';
        }
        console.log(square);
      }
    }
  }
};

module.exports = Square;
