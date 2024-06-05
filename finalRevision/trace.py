#   trace and determinant of a matrix

import numpy as np

A = np.array([
    [6, 1, 1],
    [4, -2, 5],
    [2, 8, 7]
])

B = np.trace(A)
C = np.linalg.det(A)
print(B)
print(C)