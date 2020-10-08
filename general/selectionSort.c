int selectionSort(int data[], int count) {
	int i, j;
	int tmp;
	int min;
	for (i = 0; i < count - 1; i++) {
		// Current minimum
		min = i;
		// Global minimum
		for (j = i + 1; j < count; j++) {
			if (data[min] > data[j]) {
				min = j;
			};
		};

		// Swap data[i] and data[min]
		tmp = data[i]
		data[i] = data[min]
		data[min] = tmp;
	};
	return 0;
};
