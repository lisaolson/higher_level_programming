#!/usr/bin/node
// Displays the status code of a GET request

let request = require('request');
request(process.argv[2], function (error, response) {
  if (error) {
    console.log(error);
  }
  console.log('code:', response.statusCode);
});
