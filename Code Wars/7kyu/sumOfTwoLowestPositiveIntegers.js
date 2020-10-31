/*
Create a function that returns the sum of the two lowest positive numbers given an array of minimum 4 positive integers. No floats or non-positive integers will be passed.
*/

const sumTwoSmallestNumbers = numArray => numArray.sort((a, b) => a - b);
