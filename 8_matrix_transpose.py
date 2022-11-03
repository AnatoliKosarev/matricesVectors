import numpy as np

a = np.array([[1, 2], [3, 4]])
b = np.transpose(a)
# or
c = a.T

print ("Матрица:\n", a)
print ("Транспонирование функцией:\n", b)
print ("Транспонирование методом:\n",  c)