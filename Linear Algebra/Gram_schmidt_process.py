from Vectors import Vector, dot_product, vector_addition, vector_subtraction


def normalize_vector(vector):
	v = Vector(vector)
	vect_mag = v.vector_magnitude()

	for i in range(len(vector)):
		vector[i] = vector[i] / vect_mag
	return vector


def projection_onto_orthonorm_subspace(vector, orthonorm_basis):

	for i in range(len(orthonorm_basis)):
		scalar = dot_product(vector, orthonorm_basis[i])
		v = Vector(orthonorm_basis[i])
		scal_vect_product = v.vectorScalarProduct(scalar)

		if i == 0:
			result_vector = scal_vect_product
		else:
			result_vector = vector_addition(result_vector, scal_vect_product)
	return result_vector


def construct_orthonormal_set(basis_vectors):
	no_of_basis = len(basis_vectors)
	orthonormal_basis_set = []

	for basis_num in range(no_of_basis):

		if basis_num == 0:
			orthonormal_basis_set.append(normalize_vector(basis_vectors[basis_num]))

		else:
			proj_onto_orthonorm_sub = projection_onto_orthonorm_subspace(basis_vectors[basis_num], orthonormal_basis_set)
			orthogonal_vect = vector_subtraction(basis_vectors[basis_num], proj_onto_orthonorm_sub)
			print(orthogonal_vect)
			orthonormal_basis_set.append(normalize_vector(orthogonal_vect))

	return orthonormal_basis_set


ch = construct_orthonormal_set([[-1,1,0], [-1,0,1]])
print(dot_product(ch[0], ch[1]))
# print(projection_onto_orthonorm_subspace([-1,0,1], [normalize_vector([-1,1,0])]))