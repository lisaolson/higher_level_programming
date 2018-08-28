#!/usr/bin/node
let x = process.argv[2];
let i = 0;
let j = 0;
let square = '';
if (isNaN(x)) {
  console.log('Missing size');
}
for(i = 0; i < x; i++) {
  square = "";
  for(j = 0; j < x; j++) {
    square += 'X';
  }
  console.log(square);
}
