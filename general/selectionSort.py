def selection_sort(arr):
	for index in range(0, len(arr)):
		jmin = index

		for jndex in range(index + 1, len(arr)):
			if arr[jndex] < arr[jmin]:
				jmin = jndex

		if jmin != index:
			temp = arr[index]
			arr[index] = arr[jmin]
			arr[jmin] = temp
		
	return arr
