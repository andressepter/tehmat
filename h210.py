import sys; sys.path.append('/home/asepter/.local/lib/python3.10/site-packages/')
import galois as galois
import numpy as np
import galois

korpus = galois.GF(2)

C = korpus([
    [0, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 0, 1],
    [0, 0, 1, 0, 1, 1],
    [0, 1, 1, 1, 1, 0],
    [1, 0, 0, 1, 1, 0],
    [1, 1, 0, 0, 1, 1],
    [1, 0, 1, 1, 0, 1],
    [1, 1, 1, 0, 0, 0]  
    
])

print(C)