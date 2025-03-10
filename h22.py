import sys; sys.path.append('/home/asepter/.local/lib/python3.10/site-packages/')
import galois as galois
import numpy as np
import tabulate

#korpus 3st elemendist
# 1 elementide arv, teine on aste
korpus3 = galois.GF(3)
#korpus2 = galois.GF(2,3)???

f=galois.Poly([1,0,1], field=korpus3);
#print ("polynoom ", f)
#print ("Taandumatu?", f.is_irreducible())

print(korpus3.properties)

korpus3_2 = galois.GF(3**2, repr="poly") #alternatiivne kirjutus 3**2
print(korpus3_2.properties)
#kontrollisk
#print (tabulate.tabulate("elemendid: {0,1,2,x,x+1,x+2,2x,2x+1,2x+2}"))
#elements = galois.Poly ([0, 1, 2, 'x', 'x+1', 'x+2', '2x', '2x+1', '2x+2'])
elements = korpus3_2.elements

#print (tabulate.tabulate(elements))

for element in elements:
    print (elements[4]+element)
# liita ja korrutada yle tsykilite / delo tehniki 
for element in elements:
    print (elements[4]*element)
    
#fancy grid + galois.poly ei mängi koos
# ilusama tabeli tegemist vaata naide24.py
