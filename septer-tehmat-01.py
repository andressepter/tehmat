import sys; sys.path.append('/home/asepter/.local/lib/python3.10/site-packages/')
import galois as galois
import numpy as np
import matplotlib.pyplot as plt

u = np.array([1, 0, -1, 1, 0, -1])
N = 6  # Period

# Compute the Discrete Fourier Transform (DFT) of the signal
U = np.fft.fft(u, N)

# Compute the frequency bins
frequencies = np.fft.fftfreq(N)

# Plot the magnitude spectrum
plt.stem(frequencies, np.abs(U))
plt.xlabel('Frequency')
plt.ylabel('Magnitude')
plt.title('Discrete Periodic Signal Spectrum')
plt.grid(True)
plt.show()

amplitude_spectrum = np.abs(U)

phase_spectrum = np.angle(U)

plt.figure()
plt.stem(frequencies, amplitude_spectrum)
plt.xlabel('Frequency')
plt.ylabel('Amplitude')
plt.title('Amplitude Spectrum')
plt.grid(True)

# Plot the phase spectrum
plt.figure()
plt.stem(frequencies, phase_spectrum)
plt.xlabel('Frequency')
plt.ylabel('Phase (radians)')
plt.title('Phase Spectrum')
plt.grid(True)

plt.show()

# Print the amplitude and phase spectrum for reference
print("Amplitude Spectrum:", amplitude_spectrum)
print("Phase Spectrum:", phase_spectrum)


print("DFT:", U)