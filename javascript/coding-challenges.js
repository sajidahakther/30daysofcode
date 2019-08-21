// Challenge 1
// Compare two BMI's and print whether person 1 has a greater BMI than person 2.
var janeBMI;
var alexBMI;
var janeMass = 70;
var alexMass = 80;
var janeHeight = 1.77;
var alexHeight = 1.81;

janeBMI = janeMass / (janeHeight * janeHeight);
alexBMI = alexMass / (alexHeight * alexHeight);

console.log("Is Jane's BMI greater than Alex?");
var answer = janeBMI > alexBMI;

if (janeBMI > alexBMI) {
  console.log(answer + ", Jane's BMI is greater by " + (janeBMI - alexBMI));
} else {
  console.log(answer + ", Alex's BMI is greater by " + (alexBMI - janeBMI));
}

// Challenge 2
// There are 3 teams competing at a Sports game, print out all the different scenario's of which team wins/draws.
var a = [9580, 820, 1593];
var b = [1640, 1620, 834];
var c = [1620, 250, 6193];

ameliaScore = (a[0] + a[1] + a[2]) / 3;
bellaScore = (b[0] + b[1] + b[2]) / 3;
calvinScore = (c[0] + c[1] + c[2]) / 3;

var ameliaWins = ameliaScore > bellaScore && ameliaScore > calvinScore;
var bellaWins = bellaScore > ameliaScore && bellaScore > calvinScore;
var calvinWins = calvinScore > ameliaScore && calvinScore > bellaScore;
var allDraw = ameliaScore == bellaScore && ameliaScore == calvinScore;
var draw =
  (ameliaScore == bellaScore) |
  (ameliaScore == calvinScore) |
  (bellaScore == calvinScore);

if (ameliaWins) {
  console.log("Amelia's team has won. They scored: " + ameliaScore);
} else if (bellaWins) {
  console.log("Bella's team has won. They scored: " + bellaScore);
} else if (calvinWins) {
  console.log("Calvin's team has won. They scored: " + calvinScore);
} else if (draw) {
  if (ameliaScore == bellaScore && draw != allDraw) {
    console.log(
      "Its a draw between Amelia's team and Bella's team. They both scored: " +
        ameliaScore
    );
  } else if (ameliaScore == calvinScore && draw != allDraw) {
    console.log(
      "Its a draw between Amelia and Calvin. They both scored: " + ameliaScore
    );
  } else if (allDraw) {
    console.log(
      "Its a draw between Amelia, Bella and Calvin. They all scored: " +
        ameliaScore
    );
  } else {
    console.log(
      "Its a draw between Calvin's team and Bella's team. They both scored: " +
        calvinScore
    );
  }
}
