// Exercise 4
// Add the population density to each country object in the array using the key name
// populationDensity. Population density is calculated by dividing the population by the land area.
// Refer to country-data.js to see the data format.
// spread operator ( ... ) allows you to quickly copy all or part of an existing array or object into another array or object

function exerciseFour(countriesArray) {
  const result = countriesArray.map((countries) => ({
    ...countries, // spread in the old properties
    populationDensity: countries.population / countries.landArea // add in a new property
  }));

  return result;
}

// returns
// {
//    name: 'Kenya',
//    continent: 'Africa',
//    population: 52573973,
//    landArea: 569140,
//    populationDensity: 92.37441227114594 // added the new property
// }

module.exports = exerciseFour;
