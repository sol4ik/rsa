"""
A module with help math functions needed for both encoding and decoding process.

generate_primes(n)
gcd(a, b)
"""


def generate_primes(n):
    """
    Function for generation prime numbers sequence up to n
    using the Sieve of Eratosthenes method.
    :param n: (int) the top limit for sequence generation
    :return: (list(int)) list of prime numbers
    """
    numbers = list(range(2, n))
    for i in range(len(numbers)):
        if isinstance(numbers[i], int):
            for j in range(i + 1, len(numbers)):
                if isinstance(numbers[j], int):
                    if numbers[j] % numbers[i] == 0 and numbers[j] != numbers[i]:
                        numbers[j] = '-'

    numbers = [numbers[i] for i in range(len(numbers)) if isinstance(numbers[i], int)]
    return numbers


def gcd(a, b):
    """
    Function for calculating gcd using extended Euclid method.
    :param a: (int)
    :param b: (int)
    :return: (int, int, int) gcd of a and b along with s and t: gcd(a, b) = s * a + t * b
    """
    if a == 0:
        return b, 0, 1
    else:
        g, x, y = gcd(b % a, a)
        return g, y - (b // a) * x, x
