# https://projecteuler.net/problem=9
def solution(num):
    a = 1
    b = 2
    c = num - a - b

    while c > b:
        if (a**2 + b**2) == c **2:
            print(a, b, c)
            return a*b*c
        b += 1
        c -= 1
        if b >= c:
            a += 1
            b = a + 1
            c = num - b - a


print(solution(1000))
