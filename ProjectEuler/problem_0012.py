# https://projecteuler.net/problem=12
import time

def get_n_divisors(triangle):
    n_divisors = 0
    squared_root = int(triangle ** 0.5)

    for i in range(1, squared_root + 1):
        if triangle % i == 0:
            n_divisors += 2 # Add the divisor and its compliment (triangle / i)

    # Fix perfect square
    if squared_root**2 == triangle:
        n_divisors -= 1

    return n_divisors

def triangle_with_n_divisors(n):
    if n == 1:
        return 1
    triangle = 3
    next_natural = 3
    max_n_divisors = 1
    while True:

        if(get_n_divisors(triangle) >= n):
            return triangle

        triangle += next_natural
        next_natural += 1



start_time = time.time()
print(triangle_with_n_divisors(500))
print("%.5f seconds" % (time.time() - start_time))
