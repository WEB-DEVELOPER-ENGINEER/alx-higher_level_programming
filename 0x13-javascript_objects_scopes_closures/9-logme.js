#!/usr/bin/node
exports.logMe = function logMe (item) {
  if (typeof logMe.count === 'undefined') {
    logMe.count = 0;
  }
  console.log(logMe.count + ': ' + item);
  logMe.count++;
};
