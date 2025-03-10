import sys; sys.path.append('/home/asepter/.local/lib/python3.10/site-packages/')
import galois as galois
import numpy as np
import matplotlib.pyplot as plt


u_charon = np.array([2, 2 - 2j * np.sqrt(2), 2, 2 - 2j * np.sqrt(2), 2, 2 - 2j * np.sqrt(2), 2, 2 - 2j * np.sqrt(2)])
N = 8  # Period

# Compute the amplitude spectrum
amplitude_spectrum = np.abs(u_charon)

# Compute the phase spectrum
phase_spectrum = np.angle(u_charon)

# Compute the frequency bins
frequencies = np.fft.fftfreq(N)

# Plot the amplitude spectrum
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
