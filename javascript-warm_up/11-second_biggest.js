#!/usr/bin/node
const args = process.argv.slice(2);
const numbers = args.map((arg) => parseInt(arg, 10));

if (numbers.length < 2) {
  console.log(0);
} else {
  numbers.sort((a, b) => b - a);
  console.log(numbers[1]);
}
