from PIL import Image
from numpy.random import default_rng as rng
from FourierDiscreta1D import *
from FourierDiscreta2D import *
from FourierRapide import *
import numpy as np
import cmath as math
from operators import *
import time

im = Image.open('image.jpeg').convert('L')
p = np.array(im)
#tailles
largeur, hauteur = im.size
N_org = largeur
M_org = hauteur
N = N_org + power2(N_org)
M = M_org + power2(M_org)

p = or_to_pow(p)

n = 64 #pour les tests
img1DTI = np.zeros(N, dtype=complex)
img1DTDB = np.zeros(N, dtype=complex)
img2DTI = np.zeros((M,N), dtype=complex)
img2DTDB = np.zeros((M,N), dtype=complex)

mode=2
match mode:
    case 1:
        # 1D
        p1D = np.random.rand(n)
        start_time = time.time()
        img1DTDB = FourierBrut1D(p1D)
        print("--- %s seconds Fourier Brut 1D ---" % (time.time() - start_time))
        start_time = time.time()
        img1DTI = FourierBrutInverse1D(img1DTDB)
        print("--- %s seconds Fourier Brut inverse 1D ---" % (time.time() - start_time))

        
        start_time = time.time()
        temoin1D = np.fft.fft(p1D)
        print("--- %s seconds Fourier Rapide PY 1D ---" % (time.time() - start_time))
        start_time = time.time()
        temoin1D_inv = np.fft.ifft(temoin1D)
        print("--- %s seconds Fourier Rapide INV PY 1D ---" % (time.time() - start_time))
        
        img1DTDB= traitement(img1DTDB)
        img1DTI= traitement(img1DTI)
        temoin1D = traitement(temoin1D)
        temoin1D_inv = traitement(temoin1D_inv)
        
        print("Directe :")
        comparaison(img1DTDB, temoin1D)

        print("Inverse :")
        comparaison(img1DTI, temoin1D_inv)
        
    case 2:
        start_time = time.time()
        img2DTDB = FourierBrut2D(p)
        print("--- %s seconds Fourier Brut 2D ---" % (time.time() - start_time))
        start_time = time.time()
        img2DTI = FourierBrutInverse2D(img2DTDB)
        print("--- %s seconds Fourier Brut Inv 2D ---" % (time.time() - start_time))
        start_time = time.time()
        temoin = np.fft.fft2(p)
        print("--- %s seconds Fourier Rapide PY 2D ---" % (time.time() - start_time))
        start_time = time.time()
        temoin_inv = np.fft.ifft2(temoin)
        print("--- %s seconds Fourier Rapide INV PY 2D ---" % (time.time() - start_time))
        
        temoin = traitement(temoin)
        temoin_inv = traitement(temoin_inv)
        img2DTDB = traitement(img2DTDB)
        img2DTI = traitement(img2DTI)

        print("Transformée directe : ")
        comparaison(img2DTDB, temoin) 

        print("Transformée inverse :")
        comparaison(img2DTI, temoin_inv)
        
