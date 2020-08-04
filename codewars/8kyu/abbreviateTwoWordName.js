/*
Write a function to convert a name into initials. This kata strictly takes two words with one space in between them.

The output should be two capital letters with a dot separating them.
 */

const abbreviateTwoWordName = (name) => {
	const nameList = name.split(" ");
	const initials = nameList.map(word => word[0].toUpperCase()).join(".");
	return initials
