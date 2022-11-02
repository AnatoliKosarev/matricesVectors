import numpy as np


d = np.arange(0, 24, 2)
d = d.reshape((3, 4))
print(d)

print(d[2, 1])  # or print(d[2][1]) - print 2 number from 3 line
print(d[1, :])  # or print(d[1]) - print 2 matrix line
print(d[:, 3])  # print 4 matrix column
print(d[[1, 0], [2, 3]])  # print numbers with coordinates (1, 2) and (0, 3),
                          # first array points to line, second to column

print('=============================')

# Slicing
a = np.arange(1, 13)
a = a.reshape((3, 4))
print(a)

# Используя слайсинг, созадим матрицу b из элементов матрицы а
# будем использовать 0 и 1 строку, а так же 1 и 2 столебц
# [[2 3]
#  [6 7]]
b = a[:2, 1:3]
print(b)
# BOTH MATRICES ARE LINKED TO THE SAME OBJECT AND IF VALUE CHANGED IN MATRIX B - IT WILL ALSO CHANGE FOR MATRIX A
print(a[0, 1])   # Prints "2"
b[0, 0] = 77
print(b)
print(a[0, 1])  # Prints "77"
print(a)

print('=============================')

# Integer array indexing
f = np.array([[1, 2], [3, 4], [5, 6]])
print(f)

print(f[[0, 1, 2], [0, 1, 0]])
# same as
print(np.array([f[0, 0], f[1, 1], f[2, 0]]))

print('=============================')
# Matrix slicing examples

# Example 1
g = np.arange(1, 13)
g = g.reshape((4, 3))
print(g)

g_col = np.array([0, 2, 0, 1])

# Выберем из каждой строки элемент с индексом из g_col (индекс столбца берется из g_col)
print(g[np.arange(4), g_col])
# same as
print(g[[0, 1, 2, 3], [0, 2, 0, 1]])

test = g[np.arange(4), g_col]
test[0] = 77
print(test)
print(g)

# Добавим к этим элементам 10
g[np.arange(4), g_col] += 10
print(g)

print('--------------------------------')

# Example 2

h = np.arange(1, 7)
h = h.reshape(3, 2)
print(h)

bool_idx = (h > 2)   # Найдем эллементы матрицы a, которые больше 2
                     # В результате получим матрицу b, такой же размерности, как и a

print(bool_idx)      # Prints "[[False False]
print()              #          [ True  True]
                     #          [ True  True]]"

# Воспользуемся полученным массивом для создания нового массива, ранга 1
print(h[bool_idx])  # Prints "[3 4 5 6]"

# Аналогично
print(h[h > 2])     # Prints "[3 4 5 6]"
print(h)

print('=============================')

#Помните, что вы можете пользоваться сразу несколькими типами индексирования
a = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])

row_r1 = a[1, :]
row_r2 = a[1:2, :]
print(row_r1, row_r1.shape)  # Prints "[5 6 7 8] (4,)"
print(row_r2, row_r2.shape)  # Prints "[[5 6 7 8]] (1, 4)"

row_r1[1] = 7
row_r2[0][0] = 7
print(row_r2)
print(a)