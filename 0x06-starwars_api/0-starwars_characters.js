#!/usr/bin/node

const request = require('request');
const API_URL = 'https://swapi-api.alx-tools.com/api';

if (process.argv.length > 2) {
  const movieId = process.argv[2];
  request(`${API_URL}/films/${movieId}/`, (err, response, body) => {
    if (err) {
      return console.error(err);
    }
    if (response.statusCode === 200) {
      const charactersURLs = JSON.parse(body).characters;
      const characterPromises = charactersURLs.map(url => {
        return new Promise((resolve, reject) => {
          request(url, (error, res, charBody) => {
            if (error) {
              reject(error);
            } else {
              resolve(JSON.parse(charBody).name);
            }
          });
        });
      });

      Promise.all(characterPromises)
        .then(names => {
          names.forEach(name => console.log(name));
        })
        .catch(error => console.error(error));
    } else {
      console.error(`Failed to get film data: Status code ${response.statusCode}`);
    }
  });
} else {
  console.log('Usage: ./script.js <movie_id>');
}
