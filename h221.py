import sys; sys.path.append('/home/asepter/.local/lib/python3.10/site-packages/')
import galois as galois
import numpy as np

#ei ole v2ga m6istlik kood! # * * !!!
#uncommented variant on parem ja universaalsem

korpus2_2 = galois.GF(2**4)
#base=2
#degree=4
#size=base*degree
#generate all possible vectors 
elements=korpus2_2.elements 

#k22_vectors = korpus2_2([[i, j] for i in range(base) for j in range(degree)])
#print (k22_vectors)
print (korpus2_2.irreducible_poly)

#NB! 
bit_vectors = [element.vector() for element in elements]

polynomials = [galois.Poly(vector, field=korpus2_2) for vector in bit_vectors]
#print (polynomials)

for i, value in enumerate(bit_vectors):
    print (bit_vectors[i], " ", polynomials[i])

#for vector in bit_vectors:
#    print(vector) 
#    i = enumerate(bit_vectors)
#    print (polynomials[vector])