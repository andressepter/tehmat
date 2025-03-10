import sys; sys.path.append('/home/asepter/.local/lib/python3.10/site-packages/')
import galois as galois
import numpy as np

korpus2=galois.GF(2)

G = np.array([
    [1, 0, 0, 0, 1, 1, 0],
    [0, 1, 0, 0, 0, 1, 1], 
    [0, 0, 1, 0, 1, 0, 1],
    [0, 0, 0, 1, 1, 1, 1]
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