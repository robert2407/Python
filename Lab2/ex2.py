#  2. Write a function that receives a list of numbers and returns a list of the prime numbers found in it.

import math

def test_prime(number):
    if number <= 1:
        return False

    for i in range(2, int(math.isqrt(number)) + 1):
        if number % i == 0:
            return False

    return True

def find(numbers):
    prime_numbers = []
    for i in numbers:
        if test_prime(i):
            prime_numbers.append(i)
    return prime_numbers

if __name__ == "__main__":
    prime_numbers = find([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    print("Prime numbers in the list:")
    for i in prime_numbers:
        print(i)