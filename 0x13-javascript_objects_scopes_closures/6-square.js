#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }
  print () {
    for (let i = 0; i < this.height; i++) {
      let square = '';
      for (let j = 0; j < this.width; j++) {
        square += 'X';
      }
      console.log(square);
    }
  }
  rotate () {
    let temp = this.height;
    this.height = this.width;
    this.width = temp;
  }
  double () {
    this.height = this.height * 2;
    this.width = this.width * 2;
  }
}

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c === undefined) {
        for (let i = 0; i < this.height; i++) {
            let square = '';
            for (let j = 0; j < this.width; j++) {
                square += 'C';
            }
            console.log(square);
        }
    } else {
        for (let i = 0; i < this.height; i++) {
            let square = '';
            for (let j = 0; j < this.width; j++) {
                square += 'X';
            }
            console.log(square);
        }
    }
  }
}


module.exports = Square;
