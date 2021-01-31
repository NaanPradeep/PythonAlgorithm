from Matrixv3 import *


# A ----> subspace_matrix -------> basis vectors for the subspace

def projection_on_to_subspaces(subspace_matrix, proj_vector):

	t = Matrix(subspace_matrix)
	trans_matrix = t.transpose_of_a_matrix() # A^T

	A_Atrans = matrix_multiplication(trans_matrix, subspace_matrix) # A^T x A
	s = Matrix(A_Atrans)
	A_Atrans_inv = s.inverse_of_a_matrix() # (A^T x A)^-1

	mat_mult_1 = matrix_multiplication(A_Atrans_inv, trans_matrix) # (A^T x A)^-1 X A^T
	f_transform_matrix = matrix_multiplication(subspace_matrix, mat_mult_1) #  A x (A^T x A)^-1 X A^T ---> transform_matrix(B)

	return [ddot_product(f_transform_matrix[i], proj_vector) # B x proj_vector
			for i in range(len(f_transform_matrix))
			]