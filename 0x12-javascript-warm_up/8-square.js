#!/usr/bin/node
const square_size = Math.floor(Number(process.argv[2]));
if (isNaN(square_size)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < square_size; i++) {
    let row = '';
    let j = 0;
    while (j < square_size) {
      row += 'X';
      j++;
    }
    console.log(row);
  }
}
