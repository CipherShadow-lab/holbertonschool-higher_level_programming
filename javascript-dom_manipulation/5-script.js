#!/usr/bin/node
/* Script updates text of header element to 'New Header!!!'
 * when user clicks element with id update_header */

const updateHeader = document.querySelector('header');

const setHeader = document.querySelector('#update_header');
setHeader.addEventListener('click', () => {
    updateHeader.textContent = 'New Header!!!';
});
