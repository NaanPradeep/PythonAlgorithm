def binary_search(lst, value, start, end):
	if start == end:
		return start if lst[start] < value else start + 1

	if start > end:
		return start

		


def insertion_sort(lst):
	length = len(lst)

	for i in range(1, length):
		value = lst[i]
		position = binary_search(lst, value, 0, i - 1)


def tim_sort(lst):
	length = len(lst)
	runs, sorted_run = [], []
	new_run = [lst[0]]


	for i in range(1, length):
		if i == length - 1:
			new_run.append(lst[i])
			runs.append(new_run)
			break

		if lst[i] > lst[i - 1]:
			new_run.append(lst[i])

		else:
			runs.append(new_run)
			new_run = [lst[i]]



t = tim_sort([5, 9, 10, 8, 7, 6, 7])
print(t)