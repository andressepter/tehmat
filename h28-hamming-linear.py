import numpy as np

# Function to generate Hamming (7,4) code vectors
def hamming_7_4():
    # Generator matrix for Hamming (7,4) code
    G = np.array([[1, 0, 0, 0, 1, 1, 0],
                  [0, 1, 0, 0, 1, 0, 1],
                  [0, 0, 1, 0, 0, 1, 1],
                  [0, 0, 0, 1, 1, 1, 1]])

    # Generate all possible 4-bit data vectors
    data_vectors = np.array([[int(x) for x in format(i, '04b')] for i in range(16)])

    # Calculate the code vectors
    code_vectors = np.dot(data_vectors, G) % 2

    return code_vectors

# Function to check if a code is linear
def is_linear(code_vectors):
    n = len(code_vectors)
    for i in range(n):
        for j in range(i+1, n):
            sum_vector = (code_vectors[i] + code_vectors[j]) % 2
            if not any((sum_vector == x).all() for x in code_vectors):
                return False
    return True

# Get the Hamming (7,4) code vectors
code_vectors = hamming_7_4()

# Check if the code is linear
linear = is_linear(code_vectors)

print(f"Hamming (7,4) code is {'linear' if linear else 'not linear'}.")
