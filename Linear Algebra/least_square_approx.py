from Matrixv3 import *
from Vectors import Vector
from gauss_jordan_elimination import gauss_jordan_elimination


def least_square_approx(matrix_A, vecotr_b):
	m = Matrix(matrix_A)
	trans_A = m.transpose_of_a_matrix() # A^T

	Atrans_x_A = matrix_multiplication(trans_A, matrix_A) # A^T * A
	v = Vector(vecotr_b)
	Atrans_x_bvect = v.matrix_vector_product(trans_A) # A^T * vector_b

	# finding solution for A^TA x* = A^T b
	resultant_vector = gauss_jordan_elimination(Atrans_x_A, Atrans_x_bvect) # return x*

	return resultant_vector



print(least_square_approx([[2,-1],[1,2],[1,1]], [2,1,4]))