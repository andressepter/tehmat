import sys; sys.path.append('/home/asepter/.local/lib/python3.10/site-packages/')
import galois as galois
import numpy as np

korpus=galois.GF(2**5)

C= korpus ([
    [0,0,0,0,0],
           [1,1,1,1,1],
           ])

G = korpus([
    [1, 0, 0, 1, 1],
    [0, 1, 1, 0, 1],
])

# Define the parity-check matrix H
H =korpus([
    [1, 1, 0, 1, 0],
    [0, 1, 1, 0, 1],
    [0, 0, 1, 1, 0],
    [0, 0, 0, 1, 1],
    [1, 0, 0, 0, 1],
])


y=([1,0,0,0,1],korpus)

syndrome = y @ H.T
