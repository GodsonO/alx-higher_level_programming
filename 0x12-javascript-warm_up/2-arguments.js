#!/usr/bin/node
const argument = process.argv.length;

if (argument > 2) {
  console.log('Argument' + ' found');
} else {
  console.log('No argument');
}
