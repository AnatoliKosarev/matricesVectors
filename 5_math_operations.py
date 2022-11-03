import numpy as np

x = np.array([[1, 2], [3, 4]], dtype=np.float64)
y = np.array([[5, 6], [7, 8]], dtype=np.float64)
arr = np.array([1, 2])

print(x + y)
print()
print(np.add(x, y))
print('С числом')
print(x + 1)
print('C массивом другой размерности')
print(x + arr)

print('Вычитание')
print(x - y)
print()
print(np.subtract(x, y))

print('Деление')
print(x / y)
print()
print(np.divide(x, y))

print('Other functions')
print(np.sqrt(x))