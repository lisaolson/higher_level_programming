#!/usr/bin/node
// Gets the contents of a webpage and stores it in a file

const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const ipsum = process.argv[3];

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  }
  fs.writeFile(ipsum, body, 'utf8', function (err) {
    if (err) {
      return console.log(err);
    }
  });
});
