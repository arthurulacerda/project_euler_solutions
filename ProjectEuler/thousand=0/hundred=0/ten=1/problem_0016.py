# https://projecteuler.net/problem=15
import time
from functools import reduce
import operator

def exponentiation_digits_sum(base, power):
    return reduce(operator.add,map(lambda x: int(x),list(str(base**power))))

start_time = time.time()
print(exponentiation_digits_sum(2,1000))
print("%.5f seconds" % (time.time() - start_time))
