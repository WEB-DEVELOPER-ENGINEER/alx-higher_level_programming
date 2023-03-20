#!/usr/bin/node
const Square_ = require('./5-square');
module.exports = class Square extends Square_ {
  charPrint (c) {
    if (c) {
      let prints = '';
      for (let cont = 0; cont < this.height; cont++) {
        for (let cont = 0; cont < this.height; cont++) {
          prints = prints + c;
        }
        console.log(prints);
        prints = '';
      }
    } else {
      super.print();
    }
  }
};
