# Write a NumPy program to create an element-wise comparison (equal, equal within a tolerance) of two given arrays.

import numpy as np

x = np.array([72, 79, 85, 90, 150, -135, 120, -10, 60, 100])
y = np.array([72, 79, 85, 90, 150, -135, 120, -10, 60, 100.000001])
print("Original numbers:")
print(x)
print(y)
print("Comparison - equal:")
print(np.equal(x, y))
print("Comparison - equal within a tolerance:")
print(np.allclose(x, y))

# Original numbers:
# [  72   79   85   90  150 -135  120  -10   60  100]
# [  72.         79.         85.         90.        150.       -135.
#   120.        -10.         60.        100.000001]
# Comparison - equal:
# [ True  True  True  True  True  True  True  True  True False]
# Comparison - equal within a tolerance:
# True
