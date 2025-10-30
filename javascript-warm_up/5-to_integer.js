#!/usr/bin/node
const arg = process.argv[2];
const parsedValue = parseInt(arg);
if (isNaN(parsedValue)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + parsedValue);
}
