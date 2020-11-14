# https://projecteuler.net/problem=2
def solution(input):
    a, b = 0, 1
    sum_even = 0

    while(b <= input):
        if b % 2 == 0:
            sum_even += b

        a, b = b, a + b

    return sum_even

print(solution(4000000))
# 4613732
