#!/usr/bin/node

const request = require('request');
let url = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}/`;
request(url, (error, response, body) => {
  if (error) console.error(error);
  else {
    const film = JSON.parse(body);
    console.log(film.title);
  }
});

