#!/usr/bin/node
let arg1;

if (arg1 === parseInt(process.argv[2])) {
  for (let i = 1; i <= arg1; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
