// Exercise 8
// Return true or false depending on whether all countries in the array have a population greater
// than the given threshold.
// Refer to country-data.js to see the data format.
// .every() checks if every element in an array returns true for the given function

function exerciseEight(countriesArray, populationThreshold) {
  const result = countriesArray.every(
    (country) => country.population > populationThreshold
  );
  return result;
}

module.exports = exerciseEight;
