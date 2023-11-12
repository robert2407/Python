# Write a Python class that simulates a matrix of size NxM, with N and M provided at initialization. 
# The class should provide methods to access elements (get and set methods) and some methematical functions 
# such as transpose, matrix multiplication and a method that allows iterating through all elements form a matrix an 
# apply a transformation over them (via a lambda function).

class Matrix:
    def __init__(self, rows, cols, values=None):
        self.rows = rows
        self.cols = cols
        if values:
            self.data = [[values[i * cols + j] for j in range(cols)] for i in range(rows)]
        else:
            self.data = [[0] * cols for _ in range(rows)]

    def get(self, row, col):                # returneaza valoarea
        return self.data[row][col]

    def set(self, row, col, value):         # fixeaza valoarea
        self.data[row][col] = value

    def transpose(self):
        new_matrix_trasp = Matrix(self.cols, self.rows)       # fac matricea goala cu 0
        for i in range(self.rows):
            for j in range(self.cols):
                new_matrix_trasp.set(j, i, self.get(i, j))        # o fac invers
        return new_matrix_trasp

    def multiply(self, second_matrix):
        if self.cols != second_matrix.rows:
            raise ValueError("Error, not possible to multiply")

        result = Matrix(self.rows, second_matrix.cols)      # noua matrice
        for i in range(self.rows):
            for j in range(second_matrix.cols):
                sum = 0
                for k in range(self.cols):
                    sum += self.get(i, k) * second_matrix.get(k, j)
                result.set(i, j, sum)

        return result

    def apply_transform_lambda(self, transform_func):           # aplic functia lambda
        lambda_function = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                lambda_function.set(i, j, transform_func(self.get(i, j)))

        return lambda_function

def print_matrix(matrix):
    for row in matrix.data:
        print(' '.join(map(str, row)))


if __name__ == "__main__":
    rows = 2
    cols = 4
    values = [1, 6, 3, 87, 4, 7, 23, 65]

    matrix = Matrix(rows, cols, values)

    print("Original Matrix:")
    print_matrix(matrix)

    print("\nTransposed Matrix:")
    transposed_matrix = matrix.transpose()
    print_matrix(transposed_matrix)

    print("\nMatrix Multiplication:")
    result_matrix = matrix.multiply(transposed_matrix) 
    print_matrix(result_matrix)

    print("\nApplying Transformation:")
    transformed_matrix = matrix.apply_transform_lambda(lambda x: x * 3) 
    print_matrix(transformed_matrix)