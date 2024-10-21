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
#vastuvõetud koodsõna, korpusest GF16
#NB see on teadlikult vigane sqna, et teha veaparandust
y = ff.Poly([0,0,1,0,0,0,0,1,1,0,0,1,0,0,1],field=GF16)
g = ff.Poly([1,1,1,0,1,0,0,0,1],field=GF16)

yx = lambda x: x**12+x**7+x**6+x**3+x**0
S1 = yx(a)
S2 = yx(a**2)
S3 = yx (a**3)
S4 = yx (a**4)
#primitiivse elemendi astmetena
GF16.repr("power"); 
print ('S1', S1)
print ('S2', S2)
print ('S3', S3)
print ('S4', S4)
#saame et syndroomid ei ole null, vaja on teha veaparandus
# systeemimaatriks 
M = GF16([[S1,S2],[S2,S3]])
print('derminant: ',np.linalg.det(M))
X=GF16([[S3],[S4]])
Z = np.linalg.solve(M,X)
print('lahend', Z)
#vea asukoha polynoomi funktsioon
ep = lambda x: Z[0]+x+x**2
#k + primitiivse polynoomi aste kohal k
print(list([[k,ep(a**k)] for k in range(0,15)]))
# vea polynoom genereerida

#esialgu kirjutame k2sitsi v2lja
e = ff.Poly([0,0,0,0,0,1,0,1,0,0,0,0,0,0,0],field=GF16)
C = y + e
print ('corrected word:', C)
# dekodeeritud sqnum 
DC,r = divmod( C , g)
print ('Sõnum ja jääk', DC, r)