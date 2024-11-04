#23--24
import sys; sys.path.append('/home/asepter/.local/lib/python3.10/site-packages/')
import galois as galois
import numpy as np

korpus2_3 = galois.GF(2**3, repr="power")
#repr 
elements = korpus2_3.elements

for element in elements:
        print(element.vector())
# 2.6

#redefine for clarity
korpus2_3 = galois.GF(2**3)
vectors = [korpus2_3([1, 0, 0]), korpus2_3([1, 1, 1])]
        
def linear_combinations(vectors, coefficients): 
    result = korpus2_3([0, 0, 0]) 
    for coeff, vec in zip(coefficients, vectors): 
        result += coeff * vec 
    return result

#koik
for a in range (3):
    for b in range (3):
        for c in range (3):
            coefficients = korpus2_3([a, b, c])
            linear_comb = linear_combinations(vectors, coefficients) 
            print ("lineaarkombinatsioon: ", a, " ", b, " ", c, " " )
            print(linear_comb)