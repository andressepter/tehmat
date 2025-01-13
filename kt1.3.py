import sys; sys.path.append('/home/asepter/.local/lib/python3.10/site-packages/')
import galois as galois
import numpy as np

# Define the Galois field
korpus28 = galois.GF(2**8)

# Generator matrix f
G = korpus28([
    [1, 0, 0, 1, 1, 0, 0, 1],
    [0, 1, 1, 0, 1, 0, 0, 1],
])


Ctrans = G.T

print( Ctrans)

#koodsõnad
num_codewords = Ctrans.shape[1]

print("koodsqnad", num_codewords)