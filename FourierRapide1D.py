import numpy as np
import cmath as math
from FourierDiscreta1D import *

def FourierRapide1D(img):
    N = len(img)
    if(N>2):
        pair = FourierRapide1D(img[::2])
        impair = FourierRapide1D(img[1::2])
        factor = np.exp(-2j * np.pi * np.arange(N//2) / N)
        return np.concatenate([pair + factor * impair, pair - factor * impair])
    else:
        return FourierBrut1D(img)

def FourierRapideInverse1D(img):
    N = len(img)
    if(N>2):
        pair = FourierRapideInverse1D(img[::2])
        impair = FourierRapideInverse1D(img[1::2])
        factor = np.exp(2j * np.pi * np.arange(N//2) / N)
        return np.concatenate([pair + factor * impair, pair - factor * impair])
    else:
        return FourierBrutInverse1D(img)