import numpy as np

values = np.arange(16).reshape(4, 4) * 10
print(values)
print()

view = values[:, 1:3] # this is a tuple, __get is implemented to enable this [] to work, advanced indexing
print(view)

view *= 0 # manipulate numpy array with vie
print(view)
print()
print(values)