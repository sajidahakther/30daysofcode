// Exercise 5
// Add up all the numbers in the array.

// Input is an array of numbers such as [1,2,3,4,5]
const startingAccumulator = 0;

function sum(accumulator, number) {
  return accumulator + number;
}

function exerciseFive(numbersArray) {
  let result = numbersArray.reduce(sum, startingAccumulator);
  return result;
}

// shorter way:
// function exerciseFive(numbersArray) {
//   let result = numbersArray.reduce(
//     (accumulator, number) => accumulator + number,
//     0
//   );
//   return result;
// }

module.exports = exerciseFive;
