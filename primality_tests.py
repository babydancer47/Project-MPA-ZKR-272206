"""
Primality Tests Exercises in Python

This file includes:
1. Introduction to primality tests with pseudo-code.
2. Exercises for different primality tests.
   - Each exercise includes partially complete code and tasks to fill in the blanks.
   - Exercises include specific parameters.
3. Implementation and example solutions in file solutions.py
4. Links to explanations in youtube videos.
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

# Fill the code

def sieve_of_eratosthenes(n):
    primes = [True] * (n + 1)
    primes[0] = primes[1] = _# Binary result
    for i in range(2, int(n**0.5) + 1):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = _# Binary result
    return [i for i in range(n + 1) if primes[i]]

# Evaluate sieve_of_erastosthenes for n=20



# Fermat Primality Test

# Pseudo Code

"""
FermatTest(n, iterations):
    For i = 1 to iterations:
        Choose a random 'a' in range [2, n-1]
        If gcd(a, n) != 1, continue to next iteration
        Compute r = a^(n-1) mod n
        If r != 1:
            Return "Composite"
    Return "Probably Prime"

Remember to use get_coprime() function
"""

# Fill the code

def ex_fermat_primality(n, iterations):
    for _ in range(iterations):
        a = get_coprime(n)
        # condition pow() function
            #condition return
    return True

# Evaluate Fermat Primality Test to n = 12 using your filled function. 



# Miller-Rabin Primality Test

# Pseudo-code

"""
MillerRabinTest(n, k):
    If n <= 1 or n is even, Return "Composite"
    Write n - 1 as d * 2^r (d is odd)
    For i = 1 to k:
        Choose a random 'a' in range [2, n-2]
        Compute x = a^d mod n
        If x = 1 or x = n-1, continue to next iteration
        While d != n - 1:
            Compute x = x^2 mod n
            Double d
            If x = n-1, Break
            If x = 1, Return "Composite"
    Return "Probably Prime"
"""

# Fill the code

def miller_test(d, n):
    a = random.randint(2, n - 2)
    x = power(a, d, n)
    if x == 1 or x == n - 1:
        return True
    while d != n - 1:
        x = (x * x) % n
        d *= 2
        # Condition for values of x
            # Return of possible values
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
        # Condition miller_test function
            return False
    return True

# Evaluate miller_rabin_primality for n=19,  k=4



# Lucas-Lehmer Primality Test

# Pseudo-code

"""
LucasLehmerTest(p):
    If p = 2, Return "Prime"
    Let M_p = 2^p - 1
    Set s = 4
    For i = 1 to p-2:
        Update s = (s^2 - 2) mod M_p
    If s = 0, Return "Prime"
    Else, Return "Composite"
"""

# Fill the code

def lucas_lehmer(p):
    if p == 2:
        return True
    M_p = 2**p - 1
    s = 4
    for i in range(p - 2):
        s = (s**2 - 2) # Fill the operation for value s
    return s == 0

#Evaluate lucas_lehmer for p=5


# Every exercise is solved in the file solutions.py
# Explanations for exercise in youtube:
    #Eratosthenes:  https://www.youtube.com/watch?v=klcIklsWzrY
    #Fermats:       https://www.youtube.com/watch?v=7FtAJQut4YE
    #Miller rabin:  https://www.youtube.com/watch?v=gWx9aSepqBo
    #Lucas_Lehmer:  https://www.youtube.com/watch?v=WJxAprD2QyQ