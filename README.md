
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

## Algorithms
### Sieve of Eratosthenes
Efficiently finds all prime numbers up to a given number.

### Fermat Primality Test
A probabilistic test based on Fermat's Little Theorem.

### Miller-Rabin Primality Test
A more robust probabilistic test for primality.

### Lucas-Lehmer Primality Test
Specifically designed for Mersenne numbers.
