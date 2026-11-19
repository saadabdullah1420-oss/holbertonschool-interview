#!/usr/bin/node
const request = require('request');

function getJson (url) {
  return new Promise((resolve, reject) => {
    request(url, { json: true }, (error, response, body) => {
      if (error) return reject(error);
      if (response.statusCode !== 200) {
        return reject(new Error('HTTP ' + response.statusCode));
      }
      resolve(body);
    });
  });
}

async function main () {
  const film = await getJson('https://swapi-api.hbtn.io/api/films/' + process.argv[2] + '/');
  const people = await Promise.all(film.characters.map(getJson));
  people.forEach(person => console.log(person.name));
}

main().catch(error => {
  console.error(error.message);
  process.exitCode = 1;
});
