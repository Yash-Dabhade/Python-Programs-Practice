# rite a NumPy program to test element-wise for positive or negative infinity.

import numpy as np

a = np.array([1, 0, np.nan, np.inf])
print("Original array")
print(a)
print("Test element-wise for positive or negative infinity:")
print(np.isinf(a))

"""
    output
    
    Original array
    [  1.   0.  nan  inf]
    Test element-wise for positive or negative infinity:
    [False False False  True]     
"""
