
"""
Primality Solutions in Python

This script includes implementations for:
1. Fermat Primality Test
2. Miller-Rabin Primality Test
3. Lucas-Lehmer Primality Test
4. Sieve of Eratosthenes

Each function is self-contained and can be imported or used directly.

"""

import random
from math import gcd


# Helper Functions
def get_coprime(n):
    while True:
        coprime = random.randint(2, n - 1)
        if gcd(coprime, n) == 1:
            return coprime

def power(x, y, p):
    result = 1
    x = x % p
    while y > 0:
        if y % 2 == 1:
            result = (result * x) % p
        y //= 2
        x = (x * x) % p
    return result

# Sieve of Eratosthenes
def sieve_of_eratosthenes(n):
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False
    for i in range(2, int(n**0.5) + 1):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = False
    return [i for i in range(n + 1) if primes[i]]


# Fermat Primality Test
def fermat_primality(n, iterations):
    for _ in range(iterations):
        a = get_coprime(n)
        if pow(a, n - 1, n) != 1:
            return False
    return True

# Miller-Rabin Primality Test
def miller_test(d, n):
    a = random.randint(2, n - 2)
    x = power(a, d, n)
    if x == 1 or x == n - 1:
        return True
    while d != n - 1:
        x = (x * x) % n
        d *= 2
        if x == 1:
            return False
        if x == n - 1:
            return True
    return False

def miller_rabin_primality(n, k):
    if n <= 1:
        return False
    if n <= 3:
        return True
    d = n - 1
    while d % 2 == 0:
        d //= 2
    for _ in range(k):
        if not miller_test(d, n):
            return False
    return True

# Lucas-Lehmer Primality Test
def lucas_lehmer(p):
    if p == 2:
        return True
    M_p = 2**p - 1
    s = 4
    for i in range(p - 2):
        s = (s**2 - 2) % M_p
    return s == 0

# Example usage (uncomment to test)
# print(sieve_of_eratosthenes(20)) #[2, 3, 5, 7, 11, 13, 17, 19]
# print(fermat_primality(17, 5)) #True
# print(miller_rabin_primality(19, 4)) #True
# print(miller_rabin_primality(20, 10)) #False
# print(lucas_lehmer(5)) #True