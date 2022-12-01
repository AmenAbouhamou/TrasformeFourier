from PIL import Image
import numpy as np
import cmath as math

def power2(n):
    k = 0
    while (2**k < n):
        k=k+1
    if 2**k == n:
        return 0
    else:
        return 2**k - n

def or_to_pow(t):
    m_org, n_org = t.shape
    m = m_org + power2(m_org)
    n = n_org + power2(n_org)
    t2 = np.zeros((m, n))
    for i in range(m_org):
        for j in range(n_org):
            t2[i][j]=t[i][j]
    return t2

def pow_to_or(t, m_org, n_org):#get the origin imge from the 2^n image
    m, n = t.shape
    t2 = np.zeros((m_org, n_org))
    for i in range(m_org):
        for j in range(n_org):
            t2[i][j]=t[i][j]
    return t2

def print2D(arr_2d) :
    n, m = arr_2d.shape
    for i in range(n):
        for j in range(m):
            print(arr_2d[i,j], end=" ")
        print()

def print1D(arr_2d) :
    n = len(arr_2d)
    for i in range(n):
        print(arr_2d[i], end=" ")

def print2Dresult(t):
    Im = Image.fromarray(t)
    n, m = Im.size
    #print2D(t, n, m)
    Im.show()

def traitement(arr_2d):
    t_real = arr_2d.real
    max = t_real.max()
    t = abs(t_real)
    t = t * 255/max
    t = np.round(t,0)
    return t
  
def compaire(A1,A2):
    N1,M1=A1.shape
    found=True
    for i in range(N1):
        for j in range(M1):
            k=pow((A1[i][j]-A2[i][j]),2)
            if(k>1 or k<0):
                found=False
                print(i," - ",j,"  ",A1[i][j],"   ",A2[i][j])
    if (found):
        print("C'est le bon résultat !")
    else:
        print("Ce n'est pas le bon résultat !")