import numpy as np
import cmath as math
from FourierRapide1D import *

def FFT2D(t): #MxN
    M, N = t.shape
    v = np.zeros((M, N), dtype = complex)
    w = np.zeros((M, N), dtype = complex)
    for m in range(M):
        v[m, :] = FourierRapide1D(t[m, :])
    for l in range(N):
        w[:,l] = FourierRapide1D(v[:, l])
    return w

def IFFT2D(t):
    M, N = t.shape
    v = np.zeros((M, N), dtype = complex)
    w = np.zeros((M, N), dtype = complex)
    for m in range(M):
        v[m, :] = FourierRapideInverse1D(t[m, :])
    for l in range(N):
        w[:,l] = FourierRapideInverse1D(v[:, l])
    return w
