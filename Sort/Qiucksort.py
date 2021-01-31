def quick_sort(array):

	length = len(array)
	if length <= 1:
		return array
	else:
		pivot_numb = array.pop()
		high, low = [], []

		for element in array:
			if element > pivot_numb:
				high.append(element)
			else:
				low.append(element)
	return quick_sort(low) + [pivot_numb] + quick_sort(high)


q = quick_sort([4, -2, 54, 1565, 1, 610, 1147])
print(q)
