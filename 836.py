import numpy as np

# (6) 平均10、標準偏差2の正規分布に基づく2行5列の行列
matrix = np.random.normal(loc=10, scale=2, size=(2, 5))
print("(6) 2行5列の行列:")
print(matrix)

print()

# (7) 2列目（インデックス1）の要素を抜き出す
col2 = matrix[:, 1]
print("(7) 2列目の要素:")
print(col2)
