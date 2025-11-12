#!/usr/bin/node
/* Script adds a 'li' element to a list when
 * a user clicks on element with id 'add_item' */

const listClass = document.querySelector('.my_list');

const setItem = document.querySelector('#add_item');
setItem.addEventListener('click', () => {
    const newElement = document.createElement('li');
    newElement.textContent = 'Item';
    listClass.appendChild(newElement);
});
