
# Primality Tests in Python

This repository contains Python implementations of primality tests and related algorithms, including:

1. **Sieve of Eratosthenes**
2. **Fermat Primality Test**
3. **Miller-Rabin Primality Test**
4. **Lucas-Lehmer Primality Test**


## How to Use

### Running the Script
1. Save the Python script to a file, e.g., `primality_tests.py`.
2. Run the file or import specific functions into your own scripts.

#### Example
```python
from primality_tests import fermat_primality, miller_rabin_primality

print(fermat_primality(17, 5))  # Fermat test for primality
print(miller_rabin_primality(19, 4))  # Miller-Rabin test for primality
```

### Testing
Uncomment the example usage in the Python script to see results for predefined inputs.


# Primality Test Exercises

This folder contains various exercises related to primality tests. The exercises cover the following algorithms:

1. **Sieve of Eratosthenes**
2. **Fermat's Primality Test**
3. **Miller-Rabin Primality Test**
4. **Lucas-Lehmer Primality Test**

Each exercise includes:

- **Pseudocode Explanation**: A step-by-step guide to understand the algorithm.
- **Partially Completed Implementation**: A Python code template where you need to complete the algorithm.
- **Exercise with Parameters**: A test case with specific parameter values to apply the algorithm.
- **YouTube Links**: Links to videos that explain each algorithm in detail for better comprehension.

## Folder Structure

- **primality_test.py**: Contains the exercises and explanations.
- **solutions.py**: Contains the complete and correct implementations of each algorithm. Use this file to compare and verify your solutions.

## How to Use

1. **Open the `primality_test.py` file** to view the exercises. Read through the pseudocode and try to implement the missing parts of the code.
2. **Check the test cases** provided in the exercises and implement the algorithm for each test case using the provided template.
3. **Watch the YouTube videos** linked in the `primality_test.py` file if you need further clarification on any algorithm.
4. After attempting to solve the exercise, **open the `solutions.py` file** to check the correct implementations. Compare your solution with the one provided to ensure correctness.
5. **Test your implementation** using the provided test cases and make sure it works as expected.

## Algorithms

### Sieve of Eratosthenes:

Is an ancient algorithm to find all prime numbers up to a given limit. It works by iteratively marking the multiples of each prime number starting from 2. The remaining unmarked numbers are prime.

### Fermat's Primality Test:

Is based on Fermat's Little Theorem, which states that for any integer a and a prime number p, the equation a^(p-1) ≡ 1 (mod p) holds. If a number n does not satisfy this for some a, then n is definitely composite. If it holds for several random values of a, n is probably prime, though this test can sometimes give false positives.
Miller-Rabin Primality Test:

### The Miller-Rabin test:

Is a probabilistic primality test that improves upon Fermat’s test. It works by expressing n-1 as 2^s * d and checking specific conditions to determine if n is composite. If a number passes several rounds of testing with different bases a, it is likely prime, but the test can occasionally give a false positive (hence "probabilistic").


### Lucas-Lehmer test:

Is used specifically for Mersenne primes (primes of the form 2^p - 1). It involves iterating through a recurrence relation with the initial value 4 and checking if the final result is divisible by the Mersenne number. If it is, then the number is prime; otherwise, it is composite.
