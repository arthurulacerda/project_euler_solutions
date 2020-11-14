# https://projecteuler.net/problem=3
def lasgest_prime_factor(num):
    prime_numbers = [2]

    num_factored = num

    val = 3
    while True:
        for prime in prime_numbers:
            if val % prime == 0:
                break;
        else:
            if num_factored % val == 0:
                num_factored = int(num_factored / val)
                if num_factored == 1:
                    return val
            prime_numbers.append(val)

        val += 2

print(lasgest_prime_factor(600851475143))
# 6857
