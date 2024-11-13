import sys; sys.path.append('/home/asepter/.local/lib/python3.10/site-packages/')
import galois as galois
import numpy as np
import galois

korpus = galois.GF(2)

C = korpus([
    [0, 0, 0, 0, 0, 0],
    [1, 0, 0, 1, 1, 0],
    [0, 1, 0, 1, 0, 1],
    [1, 1, 0, 0, 1, 1],
    [0, 0, 1, 0, 1, 1],
    [1, 0, 1, 1, 0, 1],
    [0, 1, 1, 1, 1, 0],
    [1, 1, 1, 0, 0, 0]
])

print(C)
#here just for reminder how it is done in python

# Function to generate the generator matrix G and parity-check matrix H
def generate_G(C):
    # Transpose of C
    C_T = C.T

    # Calculate the rank of C_T
    rank = np.linalg.matrix_rank(C_T)

    # Extract the generator matrix G from the first 'rank' rows of C_T
    G = C_T[:rank]
    
    return G.T
G_matrix = generate_G(C)

#M n d 
#n (length of codewords): 12
#M (number of codewords): 4
#d (minimum Hamming distance): 5

# Function to calculate the Hamming distance between two vectors
def hamming_distance(vec1, vec2):
    return np.sum(vec1 != vec2)

# Function to find the minimum Hamming distance in the code
def minimal_distance(C):
    min_distance = float('inf')
    n = len(C)
    for i in range(n):
        for j in range(i+1, n):
            distance = hamming_distance(C[i], C[j])
            if distance < min_distance:
                min_distance = distance
    return min_distance

# Calculate parameters n (length of codewords), M (number of codewords), and d (minimum Hamming distance)
n = C.shape[1]
M = C.shape[0]
d = minimal_distance(C)

print(f"n (length of codewords): {n}")
print(f"M (number of codewords): {M}")
print(f"d (minimum Hamming distance): {d}")
print(G_matrix)