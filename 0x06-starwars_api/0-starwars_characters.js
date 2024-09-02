#!/usr/bin/env node

const request = require ('request')

const theAPI = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}/`


request(theAPI, { json: true }, (err, res, body) => {

    const allTheCharacters = body.characters;

    for (const aCharacter of allTheCharacters) {
        request(aCharacter, { json: true }, (err, res, characterBody) => {
          console.log(characterBody.name);
        });
      }
});