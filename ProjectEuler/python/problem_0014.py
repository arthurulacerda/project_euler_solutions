# https://projecteuler.net/problem=14
import time

def odd_rule(number):
    return 3 * number + 1

def even_rule(number):
    return int(number / 2)

def chain_size(number):
    size = 1
    while number != 1:
        if(number % 2 == 0):
            number = even_rule(number)
        else:
            number = odd_rule(number)
        size += 1
    return size

def largest_chain(upper):
    largest_size = 0
    chain_number = -1
    for i in range(1,upper):
        print(i)
        current_size = chain_size(i)
        if current_size > largest_size:
            largest_size = current_size
            chain_number = i
    return i

start_time = time.time()
largest_chain(1000000)
print("%.5f seconds" % (time.time() - start_time))
