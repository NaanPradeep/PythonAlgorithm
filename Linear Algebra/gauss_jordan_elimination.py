def gauss_jordan_elimination(a, b):
	n = len(a)

	for k in range(n):
		if a[k][k] == 0: # when pivot is zero
			for i in range(k+1, n):
				# checking for non zero element in the column
				if a[i][k] != 0:
					for j in range(k, n):
						# changing zero pivot row with non zero pivot row
						a[k][j], a[i][j] = a[i][j], a[k][j]
					b[k], b[i] = b[i], b[k]
					break;

		pivot = a[k][k]
		for j in range(k, n):
			# dividing the pivot row by pivot element
			a[k][j] = a[k][j]/pivot 
		b[k] = b[k]/pivot
		for i in range(n):
			if a[i][k] == 0:continue;
			if i == k:continue;	
			factor = a[i][k]
			for j in range(k, n):
				a[i][j] = a[i][j] - factor * a[k][j]
			b[i] = b[i] - factor * b[k]
	return b
