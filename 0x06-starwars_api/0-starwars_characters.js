#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];

if (!movieId) {
  console.error('Usage: ./0-starwars_characters.js <movie_id>');
  process.exit(1);
}

const url = `https://swapi.dev/api/films/${movieId}/`;

// Fetch the movie data from SWAPI
request(url, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error('Failed to fetch movie data. Status code:', response.statusCode);
    return;
  }

  // Parse the movie data
  const filmData = JSON.parse(body);
  const characterUrls = filmData.characters;

  // Fetch and print each character name in the order listed in "characters"
  characterUrls.forEach((characterUrl) => {
    request(characterUrl, (charError, charResponse, charBody) => {
      if (charError) {
        console.error('Error fetching character:', charError);
        return;
      }

      if (charResponse.statusCode !== 200) {
        console.error('Failed to fetch character data. Status code:', charResponse.statusCode);
        return;
      }

      const characterData = JSON.parse(charBody);
      console.log(characterData.name);
    });
  });
});

