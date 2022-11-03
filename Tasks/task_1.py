import numpy as np

print('# Subtask 1')
a = np.arange(12, 43)
print(a)

print('================================')
print('# Subtask 2')
b = np.array(0 * np.arange(13))
print(b)
# or
b = np.zeros(np.array(13), int)
print(b)
b[4] = 5
print(b)

print('================================')
print('# Subtask 3')
c = np.arange(9)
c = c.reshape((3, 3))
print(c)

print('================================')
print('# Subtask 4')
a = np.array([1, 2, 0, 0, 4, 0])
print(a[a > 0])

print('================================')
print('# Subtask 5')
a = np.arange(1, 16).reshape((5, 3))
print(a)

b = np.floor(10 * np.random.random((3, 2)))
print(b)

res = a.dot(b)
print(res)

print('================================')
print('# Subtask 6')
a = np.ones((10, 10))
print(a)
print()
a[:, 0::len(a[0, :]) - 1] = 0  # change value to 0 for 1 and last column for all lines using step = len of line -1
a[0::len(a[:, 0]) - 1, :] = 0  # change value to 0 for 1 and last line for all columns using step = len of column -1
print(a)

print('================================')
print('# Subtask 7')
a = np.floor(10 * np.random.random((3, 2)))
# a = a.flatten()
print(a)
a = np.sort(a, axis=None)  # if axis None - flattens matrix, if -1 sorts each line separately
print(a)

print('================================')
print('# Subtask 8')
a = np.array([[1, 2], [3, 4]])

for index, value in np.ndenumerate(a):
    print(index, value)