def reduced_row_echelon_form(aug_matrix):
	no_of_rows = len(aug_matrix)
	no_of_cols = len(aug_matrix[0])

	c = 0 # column count --> starts with 0
	for r in range(no_of_rows): # r --> row count -->starts with 0
		# possible pivot entry is zero and its in last row.
		if aug_matrix[r][c] == 0:
			if r == no_of_rows-1:
				return aug_matrix

		if aug_matrix[r][c] == 0: # when pivot entry is zero
			for m in range(r, no_of_cols):
				for n in range(r, no_of_rows):
					# breaking the n loop since the new pivot entry is in the
					# same row as previous pivot entry(0) but a different column,
					# therefore no need for row swapping.
					if aug_matrix[n][m] != 0:
						if n == r:
							break;
					# swap rows when non zero pivot entry present in the same column but different row
					elif aug_matrix[n][m] != 0:
						aug_matrix[r], aug_matrix[n] = aug_matrix[n], aug_matrix[r]
						break;
				else:
					c += 1 # incrementing column count when there is no pivot entry in the prev column.
					continue; # continue to next column if there is no pivot entry in the current column
				break;
				
		pivot = aug_matrix[r][c]
		for j in range(r, no_of_cols):
			# dividing the row by pivot entry to make it pivot entry 1
			aug_matrix[r][j] = aug_matrix[r][j]/pivot 
		for i in range(no_of_rows):
			if aug_matrix[i][c] == 0:continue; # ignore row operation if the element in the column is 0
			if i == r:continue;	# ignore row operation in the row which contains pivot entry
			factor = aug_matrix[i][c]
			for j in range(c, no_of_cols):
				aug_matrix[i][j] = aug_matrix[i][j] - factor * aug_matrix[r][j]
		c += 1;

	return aug_matrix


print(reduced_row_echelon_form([[1,2,3,0,0,0], [0,0,1,1,0,1], [0,0,0,1,1,1]]))