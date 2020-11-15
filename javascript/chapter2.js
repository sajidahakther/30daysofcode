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

for (let i = 1; i <= 7; i++) {
  console.log("#".repeat(i))
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
Write a program that represents a 8x8 chessboard. At each posiiton of the grid there is either
a space or a # character. Adjust the program so it works for any given width and height.

 # # # #
# # # # 
 # # # #
# # # # 
 # # # #
# # # # 
 # # # #
# # # # 
*/

const width = 8;
const height = 8;
let chessboard = "";

for (let y = 1; y <= height; y++) {
  for (let x = 1; x <= width; x++) {
    if ((y + x) % 2 === 0) {
      chessboard += " ";
    }
    else {
      chessboard += "#";
    }
  }
  chessboard += "\n";
}
console.log(chessboard);
