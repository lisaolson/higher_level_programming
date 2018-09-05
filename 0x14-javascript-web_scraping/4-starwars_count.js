#!/usr/bin/node
// Print the number of movies where the character "Wedge Antilles" is present

const request = require('request');
let films = '';
request(process.argv[2], function (error, response, body) {
  if (error) {
    console.log(error);
  }
  films = JSON.parse(body).results;
  let count = 0;
  for (let i = 0; i < films.length; i++) {
    for (let j = 0; j < films[i].characters.length; j++) {
      if (films[i].characters[j] === 'https://swapi.co/api/people/18/') {
        count += 1;
      }
    }
  }
  return console.log(count);
});
