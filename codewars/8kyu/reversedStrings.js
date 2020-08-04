/*
Complete the solution so that it reverses the string passed into it.
 */

const reverseString = (text) => {
	const splitText = text.split("");
	const reversedArray = splitText.reverse();
	return reversedArray.join("");
}
