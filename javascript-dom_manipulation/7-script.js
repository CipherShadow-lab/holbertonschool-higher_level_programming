#!/usr/bin/node
/* Script fetches and lists 'title' for all movies using URL */

const filmList = document.querySelector('#list_movies');

fetch('https://swapi-api.hbtn.io/api/films/?format=json')
  .then((response) => response.json())
  .then((data) => {
      for (let index = 0; index < data.results.length; index++) {
          const newFilm = document.createElement('li');
          newFilm.textContent = data.results[index].title;
          filmList.appendChild(newFilm);
      }
  });
