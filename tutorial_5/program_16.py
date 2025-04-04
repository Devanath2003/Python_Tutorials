import numpy as np

np.random.seed(42)

array1 = np.random.randint(0, 21, size=(3, 3))
array2 = np.random.randint(0, 21, size=(3, 3))

print("Array 1:")
print(array1)
print("\nArray 2:")
print(array2)

addition_result = array1 + array2
print("\nMatrix Addition (Array1 + Array2):")
print(addition_result)

multiplication_result = np.dot(array1, array2)

print("\nMatrix Multiplication (Array1 @ Array2):")
print(multiplication_result)

elementwise_multiplication_result = array1 * array2
print("\nElement-wise Multiplication (Array1 * Array2):")
print(elementwise_multiplication_result)

transpose_of_product = multiplication_result.T

print("\nTranspose of the Matrix Multiplication Result:")
print(transpose_of_product)