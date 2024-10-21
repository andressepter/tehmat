#impordime kasutatavad teegid
import numpy as np
import galois as ff
#defineerime korpuse
GF = ff.GF(3**5)
GF2 = ff.GF(2)
GF16 = ff.GF(16)
print(GF.properties)
print(GF2.properties)
print(GF16.properties)
#korpuse karakteristik p
#degree - laiendi järk degree
# taandumatu polynoom 
# primitive_element: x
a = GF16.primitive_element
#vastuvõetud koodsõna
y = GF16.Poly([0,0,1,0,0,0,0,1,1,0,0,1,0,0,1])
yx = lambda x: x**12+x**7+x**6+x**3+x**0
S1 = yx(a)
S2 = yx(a**2)
S3 = yx (a**3)
S4 = yx (a**4)
