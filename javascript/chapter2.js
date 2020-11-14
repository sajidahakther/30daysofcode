// Exercises from the book Eloquent Javascript (3rd Edition)

/* 01. Looping a Triangle
Write a loop that makes seven calls to console.log to output the following triangle.

#
##
###
####
#####
######
#######
*/

let hash = "#";
for (let i = 1; i <= 7; i++) {
  if (i !== 1) {
    hash += "#";
  }
  console.log(hash);
}

/* 02. FizzBuzz 
Write a program that uses console.log to print all the numbers from 1 to 100, with two 
exceptions. For numbers divisible by 3, print "Fizz", for numbers divisible by 5, print 
"Buzz", for numbers divisble by both 3 and 5, print "FizzBuzz". */

for (let n = 1; n <= 100; n++) {
  if (n % 3 === 0 && n % 5 === 0) {
    console.log("Fizzbuzz");
  } else if (n % 3 === 0) {
    console.log("Fizz");
  } else if (n % 5 === 0) {
    console.log("Buzz");
  }
}

/* 03. Chessboard 
*/

const height = 8;
const width = 4;

for (let c = 1; c <= height; c++) {
  if (c % 2) {
    console.log(" #".repeat(width));
  } else {
    console.log("# ".repeat(width));
  }
}

