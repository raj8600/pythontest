import numpy as np

# Define two matrices of equal width for vertical concatenation
A = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])
B = np.array([[10, 11, 12],
              [13, 14, 15],
              [16, 17, 18]])

# Print the original matrices
print("Matrix A:")
print(A)
print("Matrix B:")
print(B)

# Concatenate the matrices vertically
C = np.concatenate((A, B), axis=0)

# Print the concatenated matrix
print("Concatenated Matrix:")
print(C)
