#!/usr/bin/node
const dict = require('./101-data.js').dict;
const Dictn = {};
for (const N in dict) {
  if (Dictn[dict[N]] === undefined) {
    Dictn[dict[N]] = [];
  }
  Dictn[dict[N]].push(N);
}
console.log(Dictn);
