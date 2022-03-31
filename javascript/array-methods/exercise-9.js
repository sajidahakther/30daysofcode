// Exercise 9
// Return true or false depending on whether there is a country in the array from a given continent.
// Refer to country-data.js to see the data format.
// .some() checks if any element in an array returns true for the given function

function exerciseNine(countriesArray, continent) {
  const result = countriesArray.some(
    (country) => country.continent === continent
  );
  return result;
}

module.exports = exerciseNine;
