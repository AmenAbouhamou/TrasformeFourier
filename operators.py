from PIL import Image
import numpy as np
import cmath as math

def power2 (n):
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

def or_to_square(t):
    m_org, n_org = t.shape
    if(m_org >= n_org):
        m = m_org + power2(m_org)
        n = m
    else:
        n = n_org + power2(n_org)
        m = n
    t2 = np.zeros((m, n))
    for i in range(m_org):
        for j in range(n_org):
            t2[i][j]=t[i][j]
    return t2

def pow_to_or(t, m_org, n_org):
    m, n = t.shape
    t2 = np.zeros((m_org, n_org))
    for i in range(m_org):
        for j in range(n_org):
            t2[i][j]=t[i][j]
    return t2

def normalize(tE):
    tS = tE
    norm = np.linalg.norm(tE)
    tS = tE/norm
    return tS

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

def comparaison(A1, A2):
    if (np.array_equal(A1, A2)):
        print("C'est le bon résultat !")
    else:
        print("Ce n'est pas le bon résultat !")
    
