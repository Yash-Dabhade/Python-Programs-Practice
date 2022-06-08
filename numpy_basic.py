import numpy as np

arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([7, 8, 9, 10])

print("Array 1", arr1)
arr1.shape = (2, 2)
arr2.shape = (2, 2)
print(arr1)

addition = arr1 + arr2
print("Addition of two matrices = \n", addition)

substraction = arr2 - arr1
print("Substraction of two matrices = \n", substraction)

multiplication = arr1 * arr2
print("Multiplication of two matrices = \n", multiplication)

division = arr1 / arr2
print("Division of two matrices = \n", division)

Str1 = "This is "
Str2 = "String"
str = np.char.add(Str1, Str2)

print("Concatenation of two strings = ", str)

arr = np.random.randint(10, 30, (6))
print(arr)
