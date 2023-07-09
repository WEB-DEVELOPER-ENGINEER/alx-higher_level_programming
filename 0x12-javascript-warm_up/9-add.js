#!/usr/bin/node
const args = process.argv;
const A = parseInt(args[2]);
const B = parseInt(args[3]);
if (isNaN(A) || isNaN(B)) {
  console.log('NaN');
} else {
  console.log(add(A, B));
}

function add (a, b) {
  return (a + b);
}
