#!/usr/bin/node
const list = require('./100-data.js').list;
const map1 = list.map(function (x) {
  return (x * list.indexOf(x));
});
console.log(list);
console.log(map1);
