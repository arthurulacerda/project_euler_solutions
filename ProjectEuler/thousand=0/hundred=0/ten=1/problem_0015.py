# https://projecteuler.net/problem=15
import time
from math import factorial as fat

def nxn_grid_paths(n):
    path_size = 2 * n
    return int(fat(path_size) / (fat(n) * fat(path_size - n)))

start_time = time.time()
print(nxn_grid_paths(20))
print("%.5f seconds" % (time.time() - start_time))
