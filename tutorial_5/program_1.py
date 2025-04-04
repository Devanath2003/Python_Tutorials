import numpy as np

matrix1 = np.array([[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]])

matrix2 = np.array([[9, 8, 7],
                    [6, 5, 4],
                    [3, 2, 1]])

result_matrix = matrix1 + matrix2
print("Matrix 1:\n", matrix1)
print("\nMatrix 2:\n", matrix2)
print("\nSum of Matrix 1 and Matrix 2:\n", result_matrix)

transpose_result = result_matrix.T

print("\nTranspose of the Result Matrix:\n", transpose_result)