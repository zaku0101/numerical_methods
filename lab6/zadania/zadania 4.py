import numpy as np
import matplotlib . pyplot as plt
from time import time
from algos import *
from scipy import optimize
import timeit

A= np.array ([[-1 ,2] ,[0 ,-1] ,[1 ,0] ])
f = np.array ([1.9, 1.5 ])
b = np.array ([0 ,-3 ,6.4 ])
bounds = [(0, None), (0, None)]
start_custom = timeit.default_timer()
print(custom_linprog(f, A, b, bounds))
stop_custom = timeit.default_timer()

start_simplex = timeit.default_timer()
print(simplex(f, A, b, bounds, maximize=True))
stop_simplex = timeit.default_timer()
print("Custom time: ", stop_custom - start_custom)
print("Simplex time: ", stop_simplex - start_simplex)