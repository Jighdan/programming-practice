/*
Remove a part of a given array between given 0-based indexes l and r (inclusive).
*/

const removeArrayPart = (inputArray, l, r) => {
	inputArray.splice(l, (r + 1 - l));
	return inputArray;
};
