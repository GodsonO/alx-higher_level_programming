#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

request(url, (error, response, body) => {
  if (error) { console.log(error); }
  const result = JSON.parse(body);
  for (const charURL of result.characters) {
    request(charURL, (error, response, body) => {
      if (error) { console.log(error); }
      const result = JSON.parse(body);
      console.log(result.name);
    });
  }
});
