# https://projecteuler.net/problem=15
import time
from math import factorial as fat

def nxn_grid_paths(n):
    return fat(2*n) / (fat(n)**2)

start_time = time.time()
print(nxn_grid_paths(20))
print("%.5f seconds" % (time.time() - start_time))
