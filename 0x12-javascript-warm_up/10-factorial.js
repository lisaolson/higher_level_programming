#!/usr/bin/node
function factorial (x) {
  if (process.argv.length === 2) {
    return 1;
  }
  if (x === 1) {
    return 1;
  }
  return factorial(x - 1) * x;
}
console.log(factorial(Number(process.argv[2])));
