/*
Given an array of integers, find if the array contains any duplicates.

Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct
*/

function containsDuplicate(nums: Array<number>): boolean {
	const seen: Array<number> = [];
	let answer: boolean = false;
	nums.forEach(num => {
		if (seen.includes(num)) {
			answer = true;
			return answer;
		} else {
			seen.push(num);
		}
	})
	return answer;
};

