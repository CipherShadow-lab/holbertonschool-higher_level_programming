#!/usr/bin/node
/* Script adds class 'red' to the header element when
 * user clicks on tag with id 'read_header' */

const headColor = document.querySelector('header');

const setColor = document.querySelector('#red_header');
setColor.addEventListener('click', () => {
    headColor.classList.add('red');
});
