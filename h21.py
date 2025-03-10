import sys; sys.path.append('/home/asepter/.local/lib/python3.10/site-packages/')
import galois as galois
import numpy as np

#korpus
korpus2 = galois.GF(2)

f=galois.Poly([1,0,1,1])
print (f)
print (f.is_irreducible())

#n2ide 2
korpus5=galois.GF(5)
f=galois.Poly([1,0,1,1], field=korpus5);
print (f)
print (f.is_irreducible())

#n2ide 3
f=galois.Poly([1,0,0,4,1], field=korpus5);
print (f)
print (f.is_irreducible())
print (f.factors())

#ylesanne 2.1 
f=galois.Poly([1,0,1], field=korpus5);
print (f)
print (f.is_irreducible())
print (f.factors())

korpus13=galois.GF(13)
f=galois.Poly([1,0,1], field=korpus13);
print (f)
print (f.is_irreducible())
print (f.factors())

#korpus13 = galois.GF(13)
#print (list(galois.irreducible_polys(5,2)))