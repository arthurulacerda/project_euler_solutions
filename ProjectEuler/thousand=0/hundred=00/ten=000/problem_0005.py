# https://projecteuler.net/problem=5
def solution(lower, upper):
    value = upper

    while True:
        for divisor in range(lower, upper + 1):
            if(value % divisor != 0):
                break;
        else:
            return value

        value += upper

print(solution(1,20))
# 232792560
