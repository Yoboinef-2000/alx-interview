#!/usr/bin/node

const request = require('request');

const theAPI = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}/`;

request(theAPI, { json: true }, (err, res, body) => {
  if (err) {
    return console.error('Error Here! Error Here!:', err);
  }
  const allTheCharacters = body.characters;

  for (const aCharacter of allTheCharacters) {
    request(aCharacter, { json: true }, (err, res, characterBody) => {
      if (err) {
        return console.error('Error Here! Error Here!', err);
      }
      console.log(characterBody.name);
    });
  }
});
