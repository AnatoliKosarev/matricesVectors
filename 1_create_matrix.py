import numpy as np


a = np.array([1, 2, 3])   # Создаем одномерный массив
print(type(a))            # Prints "<class 'numpy.ndarray'>"
print(a.shape)            # Prints "(3,)" - кортеж с размерностями
print(a[0], a[1], a[2])   # Prints "1 2 3"
a[0] = 5                  # Изменяем значение элемента массива
print(a)                  # Prints "[5, 2, 3]"

print('=============================')

b = np.array([[1, 2, 3], [4, 5, 6]])    # Создаем двухмерный массив
print(b.shape)                     # Prints "(2, 3)"
print(b[0, 0], b[0, 1], b[1, 0])   # Prints "1 2 4"

print('=============================')
# Способы создания предзаполненных матриц
c = np.eye(5)
print(c)
print()
d = np.eye(N=2, M=3)
print(d)
print()
e = np.zeros((3, 2))
print(e)
print()
f = np.ones((2, 4))
print(f)
print()
g = np.full((2, 3), 7)
print(g)
print()
h = np.random.random((2, 2))
print(h)

print('=============================')

print(np.arange(1, 5))  # Cоздает одномерную матрицу с эелементами от 1 до 4
print(type(np.arange(1, 3)))  # <class 'numpy.ndarray'>
k = np.arange(start=0, stop=24, step=2)
print(k)
k = k.reshape((3, 4))  # на базе одномерной матрицы создает матрицу 3х4
print(k)
