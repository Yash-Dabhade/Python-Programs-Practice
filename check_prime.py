from math import sqrt

# n is the number to be check whether it is prime or not
n = int(input("Enter a number : "))

# this flag maintains status whether the n is prime or not
prime_flag = 0

if n > 1:
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            prime_flag = 1
            break
    if prime_flag == 0:
        print("Prime Number")
    else:
        print("Not prime number")
else:
    print("false")
