#!/usr/bin/node
const arg = process.argv[2];
const parsedValue = parseInt(arg);

if (isNaN(parsedValue)) {
  console.log('Missing number of occurrences');
} else if (parsedValue > 0) {
  let output = '';
  for (let i = 0; i < parsedValue; i++) {
    output += 'C is fun\n';
  }
  console.log(output.trim());
}
