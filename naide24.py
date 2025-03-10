import sys; sys.path.append('/home/asepter/.local/lib/python3.10/site-packages/')
import galois as galois
import numpy as np

korpus2_3 = galois.GF(2**3, repr="power")
elements = korpus2_3.elements

print(korpus2_3.properties)
# ilusam tabel
print(korpus2_3.arithmetic_table("+"))
print(korpus2_3.arithmetic_table("*"))


