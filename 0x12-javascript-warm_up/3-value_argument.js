#!/usr/bin/node
if (process.argv[2] != null) {
  const arg1 = process.argv[2];
  console.log(arg1);
} else {
  console.log('No argument');
}
