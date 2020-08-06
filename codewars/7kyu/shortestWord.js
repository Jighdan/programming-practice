/*
Simple, given a string of words, return the length of the shortest word.

String will never be empty and you do not need to account for different data types.
*/

const shortestWord = (stringOfWords) => {
	const words = stringOfWords.split(" ");
	const wordsLengths = words.map(word => word.length);
	return Math.min(...wordsLengths);
}
