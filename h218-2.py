import numpy as np
import galois as FF
gf2 = FF.GF(2)
G=gf2([[1,0,1,1,0,1,1],
       [0,1,0,1,1,0,1]
       ])
print (G)
A=G[[0,1], 2:]
print("A:", A)
#yhikmaatriks maha
I=gf2(np.identity(5, dtype=int))
print(I)
H=np.concatenate((A.T,I), axis=1)
print("H: ",H)
#Kontroll:
print(np.matmul(G,H.T))


