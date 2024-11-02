import sys; sys.path.append('/home/asepter/.local/lib/python3.10/site-packages/')
import galois as galois
import numpy as np

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
print ("elemendid: {0,1,2,x,x+1,x+2,2x,2x+1,2x+2}" )
elements = [0, 1, 2, 'x', 'x+1', 'x+2', '2x', '2x+1', '2x+2']
#liitmine F3**2 j2rgi
def gf3_add(a, b):
 def gf3_add(a, b):
    if a == 0:
        return b
    if b == 0:
        return a
    if isinstance(a, int) and isinstance(b, int):
        return (a + b) % 3
    # Handle polynomial elements as strings
    if a == b:
        return 0  # x + x = 0 (or any element + itself = 0)
    return '0'  # Any two different polynomial elements sum to 0

#korrutamine F3**2
def gf3_mult(a, b):
    if a == 0 or b == 0:
        return 0
    elif a == 1:
        return b
    elif isinstance(b, int) and (a == 2):
        return (2 * b) % 3  #m2hkur
    
     # For x and its multiples
     mult_dict = {
        'x': {
            'x': 2, 
            'x+1': 'x+2', 
            'x+2': '2x', 
            '2x': 2, 
            '2x+1': 'x+1', 
            '2x+2': 'x'
        },
        'x+1': {
            'x': 'x+2', 
            'x+1': 2, 
            'x+2': '2x', 
            '2x': '2x+1', 
            '2x+1': 'x', 
            '2x+2': 'x+1'
        },
        'x+2': {
            'x': '2x', 
            'x+1': '2x+1', 
            'x+2': 2, 
            '2x': 'x+1', 
            '2x+1': 'x+2', 
            '2x+2': '2x'
        },
        '2x': {
            'x': '2x+1', 
            'x+1': 'x', 
            'x+2': 'x+1', 
            '2x': 0, 
            '2x+1': '2x+2', 
            '2x+2': 'x'
        },
        '2x+1': {
            'x': 'x+2', 
            'x+1': '2x', 
            'x+2': '2x+1', 
            '2x': 'x', 
            '2x+1': '2x+2', 
            '2x+2': 0
        },
        '2x+2': {
            'x': '2x+1', 
            'x+1': '2x', 
            'x+2': 'x', 
            '2x': 'x+1', 
            '2x+1': 0, 
            '2x+2': 2
        }
                    }
    
    return mult_dict[a][b]



 
# liitmistabel
addition_table = [[gf3_add(i, j) for j in elements] for i in elements]

# korrutustabel
multiplication_table = [[gf3_mult(i, j) for j in elements] for i in elements]


print("Liitmine:")
print("  ", " | ".join(str(e) for e in elements))
for i, row in enumerate(addition_table):
    print(str(elements[i]).ljust(3), " | ".join(str(r) for r in row))


print("\nKorrutamine:")
print("  ", " | ".join(str(e) for e in elements))
for i, row in enumerate(multiplication_table):
    print(str(elements[i]).ljust(3), " | ".join(str(r) for r in row))
