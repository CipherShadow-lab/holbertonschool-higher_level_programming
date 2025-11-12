#!/usr/bin/node
/* Script fetches from URL and displays value of 'hello'
 * from fetch in HTML element with id 'hello' */

document.addEventListener('DOMContentLoaded', () => {
    fetch('https://hellosalut.stefanbohacek.com/?lang=fr')
    .then((response) => response.json())
    .then((data) => {
        const helloContent = document.getElementById('hello');
        helloContent.textContent = data.hello;
    });
})
