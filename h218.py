import numpy as np
#see kood on korrektne

# Define the codewords matrix C for Hamming (7,2) code
C = np.array([
    [0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1]
])


G = np.array([
    [1, 0, 1, 1, 0, 1, 1],
    [0, 1, 0, 1, 1, 0, 1]
])

# Function to generate the parity-check matrix H
def generate_H(G):
    k, n = G.shape
    r = n - k
    P = G[:, k:].T
    I_r = np.eye(r, dtype=int)
    H = np.hstack((P, I_r))
    return H

# Generate the parity-check matrix H
H = generate_H(G)

print("Generator Matrix G:")
print(G)

print("\nParity-Check Matrix H:")
print(H)

print(np.matmul(G,H.T))