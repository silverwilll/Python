import numpy as np

values = np.random.rand(2, 3)
print(values)

rng = np.random.default_rng()

values2 = rng.standard_normal((4, 3))
print(values2)

print(values2.reshape(2, 6))