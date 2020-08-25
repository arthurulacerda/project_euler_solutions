# https://projecteuler.net/problem=1
def solution(N):
    m3 = 3
    m3_list = []
    while m3 < N:
        m3_list.append(m3)
        m3 += 3

    m5 = 5
    m5_list = []
    while m5 < N:
        m5_list.append(m5)
        m5 += 5

    m15 = 15
    m15_list = []
    while m15 < N:
        m15_list.append(m15)
        m15 += 15

    return sum(m3_list) + sum(m5_list) - sum(m15_list)

print(solution(1000))
# 233168
