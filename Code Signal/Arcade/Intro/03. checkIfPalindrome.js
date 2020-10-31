/*
Given the string, check if it is a palindrome
*/

const checkIfPalindrome = word => {
	const reversedWord = word.split("").reverse().join("");
	return (reversedWord == word) ? true : false;
};
