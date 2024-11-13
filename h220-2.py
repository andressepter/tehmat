import sys; sys.path.append('/home/asepter/.local/lib/python3.10/site-packages/')
import galois as galois
import numpy as np

# Define the Galois field GF(2)
GF = galois.GF(2)

# Define the parity-check matrix H
H = GF([
    [1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0],
    [1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0],
    [1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1],
])

# Define the generator matrix G
G = GF([
    [1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1],
    [0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1]    
])

# Received message
#EI KLAPI! 
received_message = GF([0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0,1])

# Calculate the syndrome
syndrome = received_message @ H.T

# Find the error pattern (assuming single-bit error correction)
error_pattern = GF.Zeros(received_message.shape)
for i in range(H.shape[1]):
    if np.array_equal(syndrome, H[:, i]):
        error_pattern[i] = 1
        break

# Correct the error
corrected_message = received_message + error_pattern

# Extract the original message
original_message = corrected_message[:G.shape[0]]

print("Received Message: ", received_message)
print("Syndrome: ", syndrome)
print("Error Pattern: ", error_pattern)
print("Corrected Message: ", corrected_message)
print("Original Message: ", original_message)
