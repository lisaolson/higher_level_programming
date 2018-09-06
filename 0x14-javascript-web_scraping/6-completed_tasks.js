#!/usr/bin/node
// Computes the number of tasks completed by user id

const request = require('request');
const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    return console.log(error);
  }
  let newObj = {};
  let todos = JSON.parse(body);
  for (let i = 0; i < todos.length; i++) {
    if (todos[i].completed === true) {
      if (newObj[todos[i].userId] === undefined) {
        newObj[todos[i].userId] = 1;
      } else {
        newObj[todos[i].userId] += 1;
      }
    }
  }
  return console.log(newObj);
});
