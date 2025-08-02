import numpy as np

values2 = np.array([[2.0, 3.2], [2.0, 3.1], [4.0, 2.5]], dtype=np.float64)

print(values2[2])

print(values2.shape)
print(values2.ndim)
print(values2.dtype)
print(len(values2))

values1 = np.zeros((2, 3))
print(values1)

values2 = np.arange(5, 10, 0.5)
print(values2)

values3 = np.linspace(3, 6, 5)
print(values3)