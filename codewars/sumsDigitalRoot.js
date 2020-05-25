/*
A digital root is the recursive sum of all the digits in a number. Given n, take the sum of the digits of n. If that value has more than one digit, continue reducing in this way until a single-digit number is produced. This is only applicable to the natural numbers.
 */

const digitalRoot = (number) => {
	let stringNum = number.toString();
	let arrayNum = new Array(...stringNum);
	let integerNum = [];
	arrayNum.forEach((num) => integerNum.push(Number(num)));
	let summedNum = integerNum.reduce((a, b) => a + b, 0);
	if (summedNum.toString().length > 1) {
		return digitalRoot(summedNum);
	} else {
		return summedNum;
	}
};

// Other Solutions //
const digitalRoot2 = (number) => {
	return (number - 1) % 9 + 1;
};