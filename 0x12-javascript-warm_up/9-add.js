#!/usr/bin/node
const args = process.argv;
let A = parseInt(args[2]);
let B = parseInt(args[3]);
if (isNaN(A) || isNaN(B)) {
  console.log('NaN');
} else {
  console.log(add(A, B));
}

function add (a, b) {
  return (a + b);
}
