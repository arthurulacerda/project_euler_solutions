# https://projecteuler.net/problem=7
def get_nth_prime(index_find):
    prime_numbers = [2]
    prime_index = 1

    val = 3
    while True:
        for prime in prime_numbers:
            if val % prime == 0:
                break;
        else:
            prime_index += 1
            if prime_index == index_find:
                return val
            prime_numbers.append(val)

        val += 2

print(get_nth_prime(10001))
# 104743
