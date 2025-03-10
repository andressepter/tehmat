import sys; sys.path.append('/home/asepter/.local/lib/python3.10/site-packages/')
import galois as galois

import numpy as np

# Function to generate Hamming (4,3) code vectors
def hamming_4_3():
    # Generator matrix for Hamming (4,3) code
    G = np.array([[1, 0, 0, 1],
                  [0, 1, 0, 1],
                  [0, 0, 1, 1]])

    # Generate all possible 3-bit data vectors
    data_vectors = np.array([[int(x) for x in format(i, '03b')] for i in range(8)])

    # Calculate the code vectors
    code_vectors = np.dot(data_vectors, G) % 2

    return code_vectors

# Function to calculate the Hamming distance between two vectors
def hamming_distance(vec1, vec2):
    return np.sum(vec1 != vec2)

# Function to find the minimal distance in the code
def minimal_distance(code_vectors):
    min_distance = float('inf')
    n = len(code_vectors)
    for i in range(n):
        for j in range(i+1, n):
            distance = hamming_distance(code_vectors[i], code_vectors[j])
            if distance < min_distance:
                min_distance = distance
    return min_distance

# Get the Hamming (4,3) code vectors
code_vectors = hamming_4_3()

# Find the minimal distance in the code
min_distance = minimal_distance(code_vectors)

print(f"The minimal distance in the Hamming (4,3) code is {min_distance}.")

#2 != 3, ei ole !!! 
