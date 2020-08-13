/*
You are given a string s that consists of only lowercase English letters. If vowels are given a value of 1 and consonants are given a value of 2, return the sum of all the letters in the input string.
*/

const countVowelConsonant = string => {
	const newString = string.toLowerCase();
	const reVowels = /[aeiou]/g;
	const reConsonants = /[bcdfghjklmnpqrstvwxyz]/g;
	
	const vowelsAmount = [...newString.matchAll(reVowels)].length;
	const consonantsAmount = [...newString.matchAll(reConsonants)].length;
	return vowelsAmount + (consonantsAmount * 2);
};
