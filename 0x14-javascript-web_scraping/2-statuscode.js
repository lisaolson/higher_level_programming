#!/usr/bin/node
// Displays the status code of a GET request

let request = require('request');
request(process.argv[2], function (error, response) {
  console.log('code:', response.statusCode);
});
