#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

request(url, async (error, response, body) => {
  if (error) { console.log(error); }
  const result = JSON.parse(body);

  for (const charURL of result.characters) {
    await new Promise((resolve, reject) => {
      request(charURL, (error, response, body) => {
        if (error) {
          reject(error);
        } else {
          console.log(JSON.parse(body).name);
          resolve();
        }
      });
    });
  }
});
