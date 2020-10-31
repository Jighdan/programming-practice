/*
Check to see if a string has the same amount of 'x's and 'o's. The method must return a boolean and be case insensitive. The string can contain any char.
*/

const exesAndOhs = string => {
	const regex = /([o])([x])/g;
	const newString = string.toLowerCase();
	const regexMatches = [...newString.matchAll(regex)];

	if (regexMatches[0] == regexMatches[1]) {
		return true
	};
	return false
};
