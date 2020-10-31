/*
In mathematics, the factorial of integer 'n' is written as 'n!'. It is equal to the product of n and every integer preceding it. For example: 5! = 1 x 2 x 3 x 4 x 5 = 120

Your mission is simple: write a function that takes an integer 'n' and returns 'n!'.

You are guaranteed an integer argument. For any values outside the positive range, return null, nil or None .

Note: 0! is always equal to 1. Negative values should return null.
*/

/*
IN  -> n: Number
OUT -> n: Number

CASES:
- IF n IS NOT GREATER THAN 0 -> RETURN null | None
- 0! IS EQUAL TO 1
*/

// Without Recursion
let factorial = (n: Number): Number | null => {
	if (n < 0) { return null; } 
	if (n == 0) { return 1; } 
	
	let output: Number = 1;
	for (let iter = 1; iter <= n; iter++) {
		output = output * iter;
	};

	return output;
};

// Recursive
let factorial = (n: Number): Number | null => {
	if ( n < 0 ) { return null };
	if ( n == 0 ) { return 1 };
	return n * factorial(n - 1);
};

