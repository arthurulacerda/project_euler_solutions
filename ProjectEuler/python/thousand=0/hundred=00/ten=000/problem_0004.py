# https://projecteuler.net/problem=4
def solution(lower, upper):

    palindromes = []

    for i in reversed(range(lower, upper + 1)):
        for j in reversed(range(lower, upper + 1)):
            result = str(i * j)

            if result == result[::-1]:
                palindromes.append(int(result))

    return max(palindromes)


print(solution(100, 999))
# 906609
