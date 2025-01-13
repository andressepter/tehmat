import sys; sys.path.append('/home/asepter/.local/lib/python3.10/site-packages/')
import galois as galois
import numpy as np


import matplotlib.pyplot as plt


u_charon = np.array([1, 1, -1, -1, 1])

# Calculate the convolution of the signal with itself
convolution = np.convolve(u_charon, u_charon)

#saaks teha ka manuaalselt, signall "tagurpidi" keerata ja nihutada ja korrutada ylekattuvused
#tegin funktsiooniga 

print (convolution)

# Plot the graph
plt.figure(figsize=(10, 5))
plt.plot(convolution)
plt.title('Convolution of the Signal Spectrum u charon with Itself')
plt.xlabel('Index')
plt.ylabel('Amplitude')
plt.grid(True)
plt.show()