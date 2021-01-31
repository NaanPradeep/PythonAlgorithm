def binary_search(array, target, min=None, max=None):
	if max is None:
		max = len(array) - 1
	if min is None:
		min = 0

	if min <= max:

		mid = (min + max) // 2

		if array[mid] == target:
			return mid

		elif array[mid] > target:
			max = mid - 1
			return binary_search(array, target, min, max)

		elif array[mid] < target:
			min = mid + 1
			return binary_search(array, target, min, max)

	else:
		return -1


array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
target = 22

search = binary_search(array, target)

if search != -1:
	print(f"The Target found at the index '{search}'")

else:
	print(f"Target Does Not exists")