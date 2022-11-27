import numpy as np
import cmath as math
from operators import *

def FourierBrut2D(img):
    M,N=img.shape
    res=np.ones((M,N),dtype=complex);
    for m in range(M):
        for n in range(N):
            somme=complex(0,0);
            for x in range(M):
                for y in range(N):
                    somme+=img[x][y]*math.exp(-2j*math.pi*((m * x / M) + (n * y / N)));
                res[m][n]=somme;
    return res;      

def FourierBrutInverse2D(img):
    M,N=img.shape
    res=np.ones((M,N),dtype=complex);
    for m in range(M):
        for n in range(N):
            somme=complex(0,0);
            for x in range(M):
                for y in range(N):
                    somme+=img[x][y]*math.exp(2j*math.pi*((m * x / M) + (n * y / N)));
            res[m][n]=somme/(M*N);
    return res;                