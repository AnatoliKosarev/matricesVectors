import numpy as np

x = np.array([1, 2])
print(x.dtype)  # int64

x = np.array([1.0, 2.0])
print(x.dtype)  # float64

x = np.array([1, 2], dtype=np.int32)
print(x.dtype)  # int32
