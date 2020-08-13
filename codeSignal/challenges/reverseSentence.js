/*
Reverse the order of words in a given string sentence. You can assume that sentence doesn't have any leading, trailing or repeating spaces.
*/

const reverseSentence = sentence => {
	const splitSentence = sentence.split(" ");
	splitSentence.reverse();
	return splitSentence.join(" ");
};

