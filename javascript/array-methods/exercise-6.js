// Exercise 6
// Objects are useful for looking up values quickly instead of having to search an array.
// Create a population object which given a country name as a key returns the population.
// Refer to country-data.js to see the data format.

function exerciseSix(countriesArray) {
  const result = countriesArray.reduce(
    (accumulator, country) => ({
      ...accumulator,
      [country.name]: country.population
    }),
    {}
  );

  // In this case, using reduce to create a new object. First, mapping through the array
  // to get each name and population and then returning a new object with those properties.
  return result;
}

// Returns:
// {
//     United Kingdom: 67530172,
//     Federated States of Micronesia: 113815,
//     Bangladesh: 163046161,
//     Nigeria: 200963599,
//     Kenya: 52573973,
//     Narnia: 97989
// }

module.exports = exerciseSix;
