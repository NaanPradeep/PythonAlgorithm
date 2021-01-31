
class Matrix:

    value_error = ValueError("Matrix not defined properly")

    def __init__(self, matrix):
        self.matrix = matrix


    @property
    def matrix(self):
        return self._matrix
    

    @matrix.setter
    def matrix(self, matrix):

        if len(matrix) != 0:
            col_len = len(matrix[0])
            if col_len == 0:
                raise self.value_error

            for row in matrix:
                if len(row) != col_len:
                    raise self.value_error
                for value in row:
                    if not isinstance(value, (int, float)):
                        raise ValueError("Matrix elements are not integers or float")
            self._matrix = matrix

        else:
            raise ValueError("Can't evaluate empty matrix")


    @property
    def no_of_rows(self):
        return len(self.matrix)


    @property
    def no_of_columns(self):
        return len(self.matrix[0])


    def is_square_matrix(self):
        return self.no_of_rows == self.no_of_columns


    def column_vectors(self):
        return [
            [self.matrix[column][row] for column in range(self.no_of_rows)]
            for row in range(self.no_of_columns)
        ]


    def identity(self):
        return [
            [0 if row != column else 1 for column in range(self.no_of_columns)]
            for row in range(self.no_of_rows)
        ]

    def is_invertible(self):
        return bool(self.determinant())


    # Determinant of a matrix by LU decomposition method
    def determinant_by_lu_decomposition(self):

        if not self.is_square_matrix():
            return none

        up_tri_mat = self.upper_triangular_matrix()
        product_of_diag_elmnts = 1
        for i in range(self.no_of_rows):
            product_of_diag_elmnts *= up_tri_mat[i][i]

        return product_of_diag_elmnts   


    def swap_rows(self, op_matrix, swap_row1, swap_row2):
        op_matrix[swap_row1], op_matrix[swap_row2] = op_matrix[swap_row2], op_matrix[swap_row1]

        #Multiplying the swapped row with -1
        for i in range(self.no_of_rows):
            op_matrix[swap_row2][i] *= -1
        return op_matrix


    def upper_triangular_matrix(self):
        if self.is_square_matrix():
            op_matrix_up = [self.matrix[row] for row in range(self.no_of_rows)]

            n = len(op_matrix_up)
            for k in range(n-1):
                for i in range(k+1, n):

                    # Checking op_matrix[k][k]=0 to prevent zerodivision error 
                    # and swapping rows with a non-zero element in the same column
                    if op_matrix_up[k][k] == 0:
                        for m in range(k, n):
                            if op_matrix_up[m][k] != 0:
                                op_matrix_up = self.swap_rows(op_matrix_up, m, k)
                                break;

                    #Skipping if op_matrix[i][k] = 0    
                    if op_matrix_up[i][k] == 0:continue;

                    factor = op_matrix_up[i][k]/op_matrix_up[k][k]
                    for j in range(k, n):
                        op_matrix_up[i][j] = op_matrix_up[i][j] - factor * op_matrix_up[k][j] 
            return op_matrix_up



    def inverse_of_a_matrix(self):
        if self.is_square_matrix():
            op_matrix = [self.matrix[row] for row in range(self.no_of_rows)]
            identity_matrix = self.identity()

            n = len(op_matrix)
            for k in range(n):
                if op_matrix[k][k] == 0:
                    for m in range(k+1, n):
                        if op_matrix[m][k] != 0:
                            op_matrix[m], op_matrix[k] = op_matrix[k], op_matrix[m]
                            identity_matrix[m], identity_matrix[k] = identity_matrix[k], identity_matrix[m]
                            break;
                pivot = op_matrix[k][k]
                for s in range(k, n):
                    op_matrix[k][s] = op_matrix[k][s] / pivot
                for t in range(n):  
                    identity_matrix[k][t] = identity_matrix[k][t] / pivot

                for i in range(n):
                    if op_matrix[i][k] == 0: continue;
                    if i == k: continue;
                    factor = op_matrix[i][k]
                    for j in range(n):
                        op_matrix[i][j] = op_matrix[i][j] - factor * op_matrix[k][j]
                        identity_matrix[i][j] = identity_matrix[i][j] - factor * identity_matrix[k][j]
            return identity_matrix


    
    def transpose_of_a_matrix(self):
        return [[self.matrix[j][i] for j in range(self.no_of_rows)]
                    for i in range(self.no_of_columns)
                ]



def ddot_product(vector1, vector2):
    if len(vector1) == len(vector2):
        return sum(
                    vector1[i] * vector2[i]
                    for i in range(len(vector1))
            )


# multiplying A with B ---> AB
def matrix_multiplication(A, B):
    if len(A[0]) == len(B):
        m = Matrix(B)
        colVectorsOfB = m.column_vectors()  

        return [[ddot_product(A[i], colVectorsOfB[j]) for j in range(len(B[0]))]
                    for i in range(len(A))
                    ]




# m = Matrix([[1,2,2,1],[1,2,4,2],[2,7,5,2],[-1,4,-6,3]])
# print(m.inverse_of_a_matrix())

# print(matrix_multiplication([[1,0,0,1], [0,1,0,1]], [[1,0], [0,1], [0,0], [1,1]]))
