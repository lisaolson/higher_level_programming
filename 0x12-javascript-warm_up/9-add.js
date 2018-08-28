#!/usr/bin/node
let first = Number(process.argv[2]);
let second = Number(process.argv[3]);
function add(a, b) {
  return (a + b);
}
console.log(add(first, second));
