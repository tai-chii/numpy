import numpy as np

matrix6 = np.random.normal(loc=10, scale=2, size=(2, 5))
matrix9 = np.random.rand(5, 2)

print("(6) 2行5列の行列:")
print(matrix6)
print()
print("(9) 5行2列の行列:")
print(matrix9)
print()
print("行列の積 (2x5) @ (5x2) = (2x2):")
print(np.dot(matrix6, matrix9))
