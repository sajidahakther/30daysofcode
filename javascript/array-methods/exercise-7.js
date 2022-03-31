// Exercise 7
// Return the first object in the array which matches the given name.
// Refer to country-data.js to see the data format.
// .find() returns the first element in an array that returns true for a given function

function exerciseSeven(countriesArray, countryName) {
  const result = countriesArray.find((country) => country.name === countryName);
  return result;
}

module.exports = exerciseSeven;
