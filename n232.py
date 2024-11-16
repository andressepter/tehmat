import sys; sys.path.append('/home/asepter/.local/lib/python3.10/site-packages/')
import galois as galois
import numpy as np

# 
y=galois.GF(2**15)
bch=galois.BCH(15,7)
#print(bch)
y=bch.field([1,1,1,1,1,1,1,1,1,1,0,1,1,0,0])
msg, err = bch.decode(y, errors=True)
print("message ", msg, "\t vigade arv ", err)