#!/usr/bin/node
if (isNaN(parseInt(process.argv.slice(2)))) {
  console.log(1);
} else {
  console.log(factorial(parseInt(process.argv.slice(2))));
}
function factorial (n) {
  if (n === 0) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}
