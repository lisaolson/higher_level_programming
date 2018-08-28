#!/usr/bin/node
if (typeof(process.argv[2]) === undefined) {
  console.log('Not a number');
} else {
  if (parseInt(process.argv[2] === 'NaN') {
    console.log('Not a number');
  } else {
    console.log('My number: ' + parseInt(process.argv[2], 10));
  }
}
