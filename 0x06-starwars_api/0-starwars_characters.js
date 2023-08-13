#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api';

function getCharacters (characters, index) {
  request(characters[index], (err, res, body) => {
    if (err) {
      console.log(err);
    } else {
      console.log(JSON.parse(body).name);
      if (index + 1 < characters.length) {
        getCharacters(characters, index + 1);
      }
    }
  }
  );
}

request(url + '/films/' + process.argv[2], (err, res, body) => {
  if (err) {
    console.log(err);
  } else {
    const characters = JSON.parse(body).characters;
    getCharacters(characters, 0);
  }
}
);
