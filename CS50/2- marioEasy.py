def mario_stairs(num_of_stairs):
	for step in range(1, num_of_stairs + 1):
		print((" " * (num_of_stairs - step)) + ("#" * step))
