import sys; sys.path.append('/home/asepter/.local/lib/python3.10/site-packages/')
import galois as galois
import numpy as np

# Define the Galois field
korpus28 = galois.GF(2**8)

# Generator matrix f
G = korpus28([
    [1, 0, 0, 1, 1, 0, 0, 1],
    [0, 1, 1, 0, 1, 0, 0, 1],
])

#korrektor
H = korpus28([
    [1, 1, 0, 1, 0, 0, 0, 0],
    [0, 1, 1, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 0, 1, 0, 0],
    [0, 0, 0, 1, 1, 0, 1, 0],
    [0, 0, 0, 0, 1, 1, 0, 1],
])

#m=1,0
message=korpus28([1, 0])
#kodeeritud sqnum
codeword = message @ G
print ("m kodeeritud", codeword)
# syndroom

y=([1,0,0,1,1,0,0,1])
print ("y",y)
syndrome = codeword @ H.T
print (syndrome)

# Function to calculate the Hamming distance
def hamming_distance(v1, v2):
    return np.sum(v1 != v2)


min_distance = len(y)
for i in range(2**G.shape[0]):
    message = korpus28([int(x) for x in format(i, f'0{G.shape[0]}b')])
    codeword = message @ G
    distance = hamming_distance(y, codeword)
    if distance < min_distance:
        min_distance = distance

print("Minimum Hamming Distance:", min_distance)