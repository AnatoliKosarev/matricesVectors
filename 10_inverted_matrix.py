import numpy as np

# a = np.floor(10 * np.random.random((3, 3)))
a = np.array([[1, 2, 1], [1, 1, 4], [2, 3, 6]], dtype=np.float32)
print(a)

b = np.linalg.inv(a)
print(b)

print(np.linalg.det(a))