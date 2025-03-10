import sys; sys.path.append('/home/asepter/.local/lib/python3.10/site-packages/')
import galois as galois
import numpy as np

korpus2=galois.GF(2)
poly = galois.Poly([1, 0, 0, 0, 0, 0, 0, 1], field=korpus2)
factors = poly.factors()

#voimalikud variandid
#esitus polynoomina
#Poly(x^15 + 1, GF(2))

print (factors)
print (galois.factors(poly))