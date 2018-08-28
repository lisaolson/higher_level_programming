#!/usr/bin/node
if (process.argv.length === 1) {
  console.log("0");
}
if (process.argv.length === 2) {
  console.log("0");
}
let arr = [];
for(let i = 2; i < process.argv.length; i++) {
  arr.push(Number(process.argv[i]));
}
arr = arr.sort()
console.log(arr[arr.length - 1]);
