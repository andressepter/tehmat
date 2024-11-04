import sys; sys.path.append('/home/asepter/.local/lib/python3.10/site-packages/')
import galois as galois
import numpy as np
import galois

# Define the Galois field
korpus2 = galois.GF(2)

# Generator matrix f
G = korpus2([
    [1, 0, 0, 0, 1, 1, 0],
    [0, 1, 0, 0, 1, 0, 1],
    [0, 0, 1, 0, 0, 1, 1],
    [0, 0, 0, 1, 1, 1, 1]
])

# H maatriks
H = korpus2([[
                 1, 1, 1, 0, 1, 0, 0],
                [1, 0, 1, 1, 0, 1, 0],
                [0, 1, 1, 1, 0, 0, 1]])



# All possible 4-bit messages
messages = korpus2([[i, j, k, l] for i in range(2) for j in range(2) for k in range(2) for l in range(2)])

# Encode messages using the generator matrix
codewords = [message @ G for message in messages]

# Print each codeword
for codeword in codewords:
    print(codeword)

def hamming_distance(codeword1, codeword2):
    return sum(codeword1 != codeword2)

for i in range(len(codewords)):
    if i == len(codewords):
        break
distance = hamming_distance(codewords[i], codewords[i+1]) 
print (distance)
