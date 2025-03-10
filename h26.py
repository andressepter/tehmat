import sys; sys.path.append('/home/asepter/.local/lib/python3.10/site-packages/')
import galois as galois
import numpy as np

korpus2x=galois.GF(2**9, repr="poly")

# väiksemad astmed ka 
print (list(galois.irreducible_polys(2,8)))
