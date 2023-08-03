#!/usr/bin/node

const request = require('request');
request(process.argv[2], function (error, response, body) {
  if (error) {
    console.error(error);
  }
  const users = JSON.parse(body);
  const dict = {};
  for (const user of users) {
    if (user.completed) {
      if (!dict[user.userId]) {
        dict[user.userId] = 1;
      } else {
        dict[user.userId] += 1;
      }
    }
  }
  console.log(dict);
});
