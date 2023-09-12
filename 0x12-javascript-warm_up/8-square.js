#!/usr/bin/node
const squaresize = Math.floor(Number(process.argv[2]));
if (isNaN(squaresize)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < squaresize; i++) {
    let row = '';
    let j = 0;
    while (j < squaresize) {
      row += 'X';
      j++;
    }
    console.log(row);
  }
}
