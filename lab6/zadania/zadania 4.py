import numpy as np
import matplotlib . pyplot as plt
from time import time
from algos import *
from scipy import optimize

A= np.array ([[-1 ,2] ,[0 ,-1] ,[1 ,0] ])
f = np.array ([1.9, 1.5 ])
b = np.array ([0 ,-3 ,6.4 ])
tab , x_final = simplex ( f , A , b )
print ("wartość estymowana dla simplex'a: ", tab ,"\ n")
print ("Tablica dla simplex: ", x_final ,"\ n")