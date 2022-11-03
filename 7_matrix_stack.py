import random

import numpy as np

a = np.floor(10 * np.random.random((2, 2)))
b = np.floor(10 * np.random.random((2, 2)))

print(a)
print(b)
print()

c = np.vstack((a, b))
print(c)
c[[0], [0]] = 77
print(c)
print(a)
print()

d = np.hstack((b, a))
print(d)

print('===================================')

e = np.array(np.arange(10), float)
print(e)
print()

# Превратим в матрицу
e = e.reshape((5, 2))
print(e)

# Вернем обратно
e = e.flatten()
print(e)

# Другой вариант
print(e.reshape(-1))
# Превратим в марицу (9, 1)
print(e.reshape((-1, 1)))
# Превратим в марицу (1, 9)
print(e.reshape((1, -1)))
