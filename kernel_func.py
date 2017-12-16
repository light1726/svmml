import numpy as np
import math


# gaussian kennel
def gaussian_kernel(x, z, sigma):
    dist = np.linalg.norm(x - z)
    return math.exp(-dist/(2*sigma**2))


# polynomial kernel
def ploy_kernel(x, z, c, d):
    prod = sum(x[:]*z[:])
    return pow(prod+c, d)
