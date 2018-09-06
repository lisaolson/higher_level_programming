#!/usr/bin/node
// Print the title of a Star Wars movie

const request = require('request');
const url = 'http://swapi.co/api/films/' + process.argv[2];
let films = '';

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  }
  films = JSON.parse(body).characters;
  for (let i = 0; i < films.length; i++) {
    let charUrl = films[i];
    request(charUrl, function (error, response, body) {
      if (error) {
        console.log(error);
      }
      console.log(JSON.parse(body).name);
    });
  }
});
