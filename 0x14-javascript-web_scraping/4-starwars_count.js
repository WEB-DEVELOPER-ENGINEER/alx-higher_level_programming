#!/usr/bin/node

const request = require('request');
let i = 0;
request(process.argv[2], (error, response, body) => {
  if (error) console.error(error);
  const films = JSON.parse(body);
  for (const film of films.results) {
    if (film.characters.includes('https://swapi-api.alx-tools.com/api/people/18/')) {
      i += 1;
    }
  }
  console.log(i);
});
