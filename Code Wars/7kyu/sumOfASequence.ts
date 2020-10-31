/*
Your task is to make function, which returns the sum of a sequence of integers.

The sequence is defined by 3 non-negative values: begin, end, step.

If begin value is greater than the end, function should returns 0
*/

/*
IN  -> (begin: Number, end: Number, step: Number)
OUT -> (sumOfSequence: Number)

CASES:
- IF begin IS GREATER-THAN end -> RETURN 0
*/

// Non Recursive
let sumOfSequence = (begin: Number, end: Number, step: Number): Number => {
	let output: Number = 0;
	if (begin < end) {
		for (let iter = begin; iter <= end; iter = iter + step) {
			output = output + iter;
		};
	} ;

	return output;
};

// Recursive
let sumOfSequence = (begin: Number, end: Number, step: Number): Number => {
	if (begin > end) { return 0 };
	return begin + sumOfSequence(begin + step, end, step);
};

