import sys; sys.path.append('/home/asepter/.local/lib/python3.10/site-packages/')
import galois as galois
import numpy as np

korpus = galois.GF(2)

C = korpus([
    [0, 0, 0],
    [1, 1, 1]
])

# Function to calculate the Hamming distance between two vectors
def hamming_distance(vec1, vec2):
    return np.sum(vec1 != vec2)

# Calculate the Hamming distance between the given vectors
distance = hamming_distance(C[0], C[1])

n = C.shape[1]
M = C.shape[0]

print ("n", n)
print ("M", M)
print ("d", distance)

# Function to generate all possible vectors in GF(2)^n
def generate_all_vectors(n):
    return np.array([[int(x) for x in format(i, f'0{n}b')] for i in range(2**n)])

# Function to check if a code is perfect
def is_perfect_code(C):
    n = C.shape[1]
    M = C.shape[0]
    
    # Generate all possible vectors in GF(2)^n
    all_vectors = generate_all_vectors(n)
    
    # Calculate the covering radius
    covering_radius = 0
    for vector in all_vectors:
        min_distance = float('inf')
        for codeword in C:
            distance = hamming_distance(vector, codeword)
            if distance < min_distance:
                min_distance = distance
        if min_distance > covering_radius:
            covering_radius = min_distance
    
    # Calculate the minimum Hamming distance
    min_distance = float('inf')
    for i in range(M):
        for j in range(i+1, M):
            distance = hamming_distance(C[i], C[j])
            if distance < min_distance:
                min_distance = distance
    
    # Check if the code is perfect
    t = (min_distance - 1) // 2
    return covering_radius == t

# Check if the given code is perfect
perfect = is_perfect_code(C)

print(f"The given Hamming code is {'perfect' if perfect else 'not perfect'}.")