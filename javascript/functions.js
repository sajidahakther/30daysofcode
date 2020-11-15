// 01. Arrow Functions

const power = (base, exponent) => {
  let result = 1;
  for (let count = 0; count < exponent; count++) {
    result *= base;
  }
  return result;
}

console.log(power(2, 10));

// When there is only one parameter you can omit the parentheses

const square = x => x * x;

console.log(square(5));

// With no parameters

const greet = () => {
  console.log("hello!")
}

greet()

/* 02. Function Declaration –– function doStuff() {};

If you don't pass a value, it will default to two. JavaScript is tolerant about the number of arguments you
pass to a function. If you pass too many, the extra ones are ignored. If you pass too few, the missing parameter
gets asigned the value 'undefined' */

function power(base, exponent = 2) {
  let result = 1;
  for (let count = 0; count < exponent; count++) {
    result *= base;
  }
  return result;
}

console.log(power(4));

/* 03. Function Expression –– const doStuff = function() {} 

Hoisting refers to the availability of functions and variables “at the top” of your code, as opposed to only after 
they are created. Function declarations are hoisted but function expressions are not. */
