#!/usr/bin/node
let arg1;

if (arg1 = parseInt(process.argv[2])) {
    let square = '';
    for (i=1; i <= arg1; i++) {
        for (j=1; j <= arg1; j++) {
            square += 'X';
        }
        square += '\n';
    }
    console.log(square);
}
else {
    console.log('Missing size');
};