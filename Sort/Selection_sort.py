def sort(array):
	length = len(array)

	for i in range(length):
		min_index = i
		for j in range(i+1, length):
			if array[j] < array[min_index]:
				min_index = j
		
		array[i], array[min_index] = array[min_index], array[i]

	return array



s = sort([4, -2, 354, 565, 1, 10])
print(s)
