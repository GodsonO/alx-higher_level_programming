#!/usr/bin/node
const argc = process.argv.length;

if (argc > 2) {
  console.log(process.argv[2]);
} else {
  console.log('No argument');
}
