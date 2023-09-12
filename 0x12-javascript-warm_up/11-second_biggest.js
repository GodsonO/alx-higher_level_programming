#!/usr/bin/node
const num = process.argv.length;

if (num <= 3) {
  console.log(0);
} else {
  const args = process.argv.map(Number)
    .slice(2, num)
    .sort((a, b) => a - b);
  console.log(args[args.length - 2]);
}
