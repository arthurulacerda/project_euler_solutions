# https://projecteuler.net/problem=10

def solution(upper)
    primes_list = set(range(3, upper + 1, 2))

    for number in range(3, int(upper ** 0.5) + 1):
        if number not in primes_list:
            continue

        num = number
        while num < upper:
            num += number
            if num in primes_list:
                primes_list.remove(num)

    return (2 + sum(primes_list))


print(solution(2000000))
