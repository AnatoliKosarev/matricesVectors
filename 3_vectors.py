import numpy as np

a = np.array([1, 2, 3])
b = np.array([[1], [2], [3]])

print ("Вектор:\n", a)
print ("Его размерность:\n", a.shape)
print ("Двумерный массив:\n", b)
print ("Его размерность:\n", b.shape)

a = a.T
b = b.T

print ("Вектор не изменился:\n", a)
print ("Его размерность также не изменилась:\n", a.shape)
print ("Транспонированный двумерный массив:\n", b)
print ("Его размерность изменилась:\n", b.shape)