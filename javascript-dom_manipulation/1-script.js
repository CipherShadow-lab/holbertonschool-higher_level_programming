#!/usr/bin/node
/* Script updates the text color of header element to red ('#FF0000')
 * when user clicks on tag with id red_header */

const headColor = document.querySelector('header');

const setColor = document.querySelector('#red_header');
setColor.addEventListener('click', () => {
    headColor.style.color = '#FF0000';
});
