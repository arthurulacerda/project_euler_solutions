# https://projecteuler.net/problem=6
def solution(upper):
    list_squares = []
    list_numbers = []

    for i in range(1,upper + 1):
        list_numbers.append(i)
        list_squares.append(i**2)

    return (sum(list_numbers)**2) - sum(list_squares)


print(solution(100))
# 104743
