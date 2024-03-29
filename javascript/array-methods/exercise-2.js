// Exercise 2
// Return all countries in the array which belong to the given continent.
// Refer to country-data.js to see the data format.

function exerciseTwo(countriesArray, continent) {
  const result = countriesArray.filter(
    (countries) => countries.continent === continent
  );

  return result;
}

module.exports = exerciseTwo;
