
import sys; sys.path.append('/home/asepter/.local/lib/python3.10/site-packages/')
import galois as galois
import numpy as np
import matplotlib.pyplot as plt

import numpy as np
# Define the continuous signal u(t)
def u(t):
    return 3 * np.sin(2 * np.pi * t) - 2 * np.sin(4 * np.pi * t)

# Define the sampling frequency
fs = 10  # Hz

# Define the time range for the sampled signal
ts = np.arange(0, 1, 1/fs)

# Sample the signal
us = u(ts)

# Plot the sampled signal
plt.figure(figsize=(12, 6))
plt.stem(ts, us, label='Sampled Signal at 10 Hz')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Sampled Signal u(t) = 3sin(2*Pi*t) - 2sin(4 * pi * t) at 10 Hz')
plt.legend()
plt.grid(True)
plt.show()