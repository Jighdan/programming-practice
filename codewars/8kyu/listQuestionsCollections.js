/*
I'm new to coding and now I want to get the sum of two arrays...actually the sum of all their elements. I'll appreciate for your help.
*/

const arrayPlusArray = (array1, array2) => Math.sum(...array1) + Math.sum(...array2);

/*
Consider an array/list of sheep where some sheep may be missing from their place. We need a function that counts the number of sheep present in the array (true means present).
*/

const countSheep = sheeps => {
	let count = 0;
	for (let item = 0; item < sheeps; item++) {
		if ( sheeps[item] == true ) {
			count++
		}
	};
	return count;
};

/*
In this kata you will create a function that takes in a list and returns a list with the reverse order.
*/

const reverseArray = array => array.reverse();

/*
Write a method sum that takes an array of numbers and returns the sum of the numbers. These may be integers or decimals for Ruby and any instance of Num for Haskell. The numbers can also be negative. If the array does not contain any numbers then you should return 0.
*/

const sumArray = array => Math.sum(...array);

/*
Given an array of integers your solution should find the smallest integer.
*/

const smallestNumber = array => Math.min(...array);

/*
There was a test in your class and you passed it. Congratulations!
But you're an ambitious person. You want to know if you're better than the average student in your class.

You receive an array with your peers' test scores. Now calculate the average and compare your score!

Return True if you're better, else False!
*/

const betterThanAverage = (classPoints, yourScore) => {
	const average = Math.sum(...classPoints) / classPoints.length();
	return (yourScore > average) ? true : false;
};

/*
Write a function findNeedle() that takes an array full of junk but containing one "needle". After your function finds the needle it should return a message (as a string) that says:
"Found the needle at position " plus the index it found the needle.
*/

const findNeedle = array => {
	const needleIndex = String(array.indexOf("needle"));
	return `Found the needle at the position ${needleIndex}`;
};

/*
Your task is to make two functions, max and min (maximum and minimum in PHP and Python) that take a(n) array/vector of integers list as input and outputs, respectively, the largest and lowest number in that array/vector.
*/

const minArray = arr => Math.min(...arr);
const maxArray = arr => Math.max(...arr);
