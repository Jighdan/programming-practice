// Make a function that returns the number of coincidences of an element in an array.

# include <stdio.h>

int main(char array, char search) {
	int index;
	int count = 0;
	for (index = 0; index < sizeof(array); index++) {
		if (search == array[index]) {
			count++;
		};
	};

	return count;
};
