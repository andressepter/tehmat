import sys; sys.path.append('/home/asepter/.local/lib/python3.10/site-packages/')
import galois as galois
import numpy as np

#ei ole v2ga m6istlik kood! 

korpus2_2 = galois.GF(2*4 repr="")
base=2
degree=4
size=base*degree
#generate all possible vectors 

k22_vectors = korpus2_2([[i, j] for i in range(base) for j in range(degree)])
print (k22_vectors)
print (korpus2_2.irreducible_poly)
polynomials = [galois.Poly(vector, field=korpus2_2) for vector in k22_vectors]
print (polynomials)
