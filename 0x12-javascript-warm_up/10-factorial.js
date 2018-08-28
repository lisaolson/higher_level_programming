#!/usr/bin/node
let arg = Number(process.argv[2]);
function factorial(x) {
  if (x < 1) {
    return 0;
  }
  if (x === 1) {
    return 1;
  }
  return factorial(x - 1) * x;
}
console.log(factorial(arg));
