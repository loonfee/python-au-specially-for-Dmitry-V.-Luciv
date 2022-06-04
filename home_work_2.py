import time
import multiprocessing
from math import cos, pi
import random as rnd
def integral(n):
    k = 0
    for _ in range(n):
        x = rnd.uniform(0, pi * 0.5)
        y = rnd.uniform(0, 1)
        if y < cos( x ):
            k += 1
    return pi * 0.5 * k/n
if __name__ == '__main__':
    timer = time.time()
    pool = multiprocessing.Pool(processes = 10)
    print("интегралл:", sum(pool.map(integral,[1000000]*10))/10)
    print("время (with multiprocessing):", time.time() - timer)
    timer = time.time()
    print("интегралл:", integral(10000000))
    print("время:", time.time() - timer)
'''если увеличить количество точек еще в 10 раз:
интегралл: 1.0000945268039585
время (with multiprocessing): 28.663557291030884
интегралл: 1.000026150039853
время: 54.45448541641235
'''