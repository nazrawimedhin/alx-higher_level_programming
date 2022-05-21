#!/usr/bin/node
function add (a, b) {
  return a + b;
}

if (process.argv.length === 4) {
  const result = add(parseInt(process.argv[2]), parseInt(process.argv[3]));
  console.log(result);
}
