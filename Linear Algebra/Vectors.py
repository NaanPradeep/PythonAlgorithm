from Matrixv3 import *

class Vector:

	value_error = TypeError("Value Error")

	def __init__(self, vector):
		self.vector = vector


	def print_vectors(self):
		return self.vector


	def vector_magnitude(self):		
		v = sum(
				self.vector[i] ** 2
				for i in range(len(self.vector))
			)
		return v ** 0.5



	def vectorScalarProduct(self, scalar_val):

		return [scalar_val * self.vector[i] for i in range(len(self.vector))]


	def matrix_vector_product(self, matrix):
		if len(self.vector) == len(matrix[0]):
			return [self.dot_product(matrix[i]) for i in range(len(matrix))]



def dot_product(vector1, vector2):
		if len(vector1) == len(vector2):
			return sum( vector1[i] * vector2[i]
						for i in range(len(vector1))
			 )


def vector_addition(vector1, vector2):
	if len(vector1) == len(vector2):
		return [vector1[i] + vector2[i]
				for i in range(len(vector1))
				]

def vector_subtraction(vector1, vector2):
	if len(vector1) == len(vector2):
		return [vector1[i] - vector2[i]
				for i in range(len(vector1))
				]








# v = Vector([2, 2, 1])
# # print(v.matrix_vector_product([[1,2,3], [4,5,6], [7,8,9]]))
# print(v.matrixMultiplication([[1,2,3], [4,5,6], [7,8,9]], [[1,2,3], [4,5,6], [7,8,9]]))
# print(v.projection_on_to_subspaces([[1,0],[0,1],[0,0],[1,1]], [1,2,3,4]))

