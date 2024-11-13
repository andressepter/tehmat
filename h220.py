import numpy as np

H=np.array([
[1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0],
[1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0],
[0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0],
[1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
[0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0],
[0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0],
[0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1],
])

G=np.array([
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
received_message = np.array([0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0,1])

# Calculate the syndrome
syndrome = np.dot(received_message, H.T) % 2

# Find the error pattern (assuming single-bit error correction)
error_pattern = np.zeros_like(received_message)
for i in range(H.shape[1]):
    if np.array_equal(syndrome, H[:, i]):
        error_pattern[i] = 1
        break

# Correct the error
corrected_message = (received_message + error_pattern) % 2

# Extract the original message
original_message = corrected_message[:G.shape[0]]

print("Received Message: ", received_message)
print("Syndrome: ", syndrome)
print("Error Pattern: ", error_pattern)
print("Corrected Message: ", corrected_message)
print("Original Message: ", original_message)