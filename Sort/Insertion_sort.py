def insertion_sort(array):
	length = len(array)

	for i in range(1, length):
		while i > 0:
			if array[i] < array[i - 1]:
				array[i], array[i - 1] = array[i - 1], array[i]
			i -= 1

	return array



i = insertion_sort([4, 15, 2, 71, 3, 11])
print(i)
