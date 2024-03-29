import numpy as np
import cmath as math

def FourierBrut1D(img):
    N=len(img)
    res=np.ones(N,dtype=complex)
    for k in range(N):
        somme=complex(0,0)
        for n in range(N):
            somme+=img[n]*math.exp(-2j*math.pi*k*n/N)
        res[k]=somme
    return res;    

def FourierBrutInverse1D(img):
    N=len(img)
    res=np.ones(N,dtype=complex)
    for k in range(N):
        somme=complex(0,0)
        for n in range(N):
            somme+=img[n]*math.exp(2j*math.pi*k*n/N)
        res[k]=somme/N
    return res;             