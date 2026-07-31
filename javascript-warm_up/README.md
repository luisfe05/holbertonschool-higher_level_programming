# JavaScript - Warm up

## Description
This project introduces JavaScript scripting fundamentals using Node.js. It covers variable declarations (`const`, `let`, `var`), basic data types, outputting with `console.log`, control flow, functions, and enforcing code quality standards using `semistandard`.

## Tasks

| Task | Description | File |
| :--- | :--- | :--- |
| **0. First constant, first print** | Write a script that creates a constant variable `myVar` with the value `"JavaScript is amazing"` and prints it using `console.log`. | `0-javascript_is_amazing.js` |
| **1. 3 languages** | Write a script that prints three lines: `"C is fun"`, `"Python is cool"`, `"JavaScript is amazing"`, each via a separate `console.log`. | `1-multi_languages.js` |
| **2. Arguments** | Write a script that prints a message depending on the number of arguments passed via `process.argv`: `"No argument"`, `"Argument found"`, or `"Arguments found"`. | `2-arguments.js` |
| **3. Value of my argument** | Write a script that prints the first argument passed to it, or `"No argument"` if none was passed (without using `length`). | `3-value_argument.js` |
| **4. Create a sentence** | Write a script that prints two arguments passed to it in the format `" is "`, using template literals. | `4-concat.js` |
| **5. An Integer** | Write a script that prints `My number: <int>` if the first argument converts to an integer via `parseInt`/`Number.isNaN`, otherwise `"Not a number"` (no `try/catch`). | `5-to_integer.js` |
| **6. Loop to languages** | Write a script that prints the 3 language lines using an array and a loop, with a single `console.log` and no `if/else`. | `6-multi_languages_loop.js` |
| **7. I love C** | Write a script that prints `"C is fun"` `x` times, where `x` is the first argument, or `"Missing number of occurrences"` if it can't be converted to an integer. | `7-multi_c.js` |
| **8. Square** | Write a script that prints a square of `X` characters sized by the first argument, or `"Missing size"` if it can't be converted to an integer. | `8-square.js` |
| **9. Add** | Write a script defining `function add(a, b)` that prints the addition of the first two arguments. | `9-add.js` |
| **10. Factorial** | Write a script that recursively computes and prints the factorial of the first argument (factorial of `NaN` is `1`). | `10-factorial.js` |
| **11. Second biggest!** | Write a script that prints the second biggest integer among the arguments, or `0` if fewer than 2 arguments are passed. | `11-second_biggest.js` |
| **12. Object** | Update a given script to change an object's `value` property from `12` to `89` without reassigning the `const` variable. | `12-object.js` |
| **13. Add file** | Write and export a reusable `add` function from a module, callable via `require('./13-add').add`. | `13-add.js` |

## Author
* **Luis Gonzalez** - Holberton School
