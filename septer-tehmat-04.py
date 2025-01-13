import sys; sys.path.append('/home/asepter/.local/lib/python3.10/site-packages/')
import galois as galois
import numpy as np
import matplotlib.pyplot as plt

# Define the time variable
t1 = np.linspace(0, 2, 1000)  # Time from 0 to 2 seconds


u_t = 3 * np.sin(2 * np.pi * t1) + np.sin(6 * np.pi * t1)

# Plot the signal
plt.figure(figsize=(10, 5))
plt.plot(t1, u_t)
plt.title('Analoogsignaal u(t) = 3sin(2πt) + sin(6πt)')
plt.xlabel('Time (t)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.show()

#diskreetimine
fs = 9  # Sampling frequency in Hz
t = np.arange(0, 1, 1/9)   # Time from 0 to 2 seconds with step size of 1/fs
u_t = 3 * np.sin(2 * np.pi * t) + np.sin(6 * np.pi * t)
print("Shape of time vector t:", t.shape)
print("Discretized signal values:", u_t)
print("Shape of signal u_t:", u_t.shape)


plt.figure(figsize=(10, 5))
plt.stem(t, u_t)
plt.plot(t, u_t, linestyle='-', marker='o', color='b')
plt.title('Discrete Signal u(t) at 9Hz')
plt.xlabel('Time (t)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.show()

#vastavus Shannoni kriteeriumile
#kindluse m6ttes arvutame uuesti

sampling_frequency = 9  # Hz
t = np.arange(0, 1, 1/sampling_frequency)  # time vector from 0 to 1 second

u_t = 3 * np.sin(2 * np.pi * t) + np.sin(6 * np.pi * t)

# fmax
max_frequency_component = 3  # The highest frequency component in the signal is 3 Hz (from sin(6 * pi * t))

nyquist_rate = 2 * max_frequency_component

if sampling_frequency >= nyquist_rate:
    print("Vastab.")
else:
    print("Ei vasta Shannonikriteeriumile.")

# Print the Nyquist rate and sampling frequency for reference
print(f"Nyquist rate: {nyquist_rate} Hz")
print(f"Sampling frequency: {sampling_frequency} Hz")

#libisev keskmine 

# Apply sliding average filter with value 2
window_size = 2
filtered_signal = np.convolve(u_t, np.ones(window_size)/window_size, mode='valid')

# Plot the original and filtered signals
plt.figure()
plt.stem(t, u_t, label='Original Signal', basefmt=" ")
plt.stem(t[:len(filtered_signal)], filtered_signal, label='Filtered Signal', basefmt=" ", linefmt='r-', markerfmt='ro')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Original and Filtered Signal')
plt.legend()
plt.grid(True)
plt.show()

# Print the filtered signal values
print("Filtered signal values:", filtered_signal)

#see ylesanne on suurem kui terve eksam
#umbumine ja faasinihe
# DFT
U_original = np.fft.fft(u_t)
U_filtered = np.fft.fft(filtered_signal, n=len(U_original))


frequencies = np.fft.fftfreq(len(U_original), d=1/sampling_frequency)

# Calculate the amplitude spectrum
amplitude_spectrum_original = np.abs(U_original)
amplitude_spectrum_filtered = np.abs(U_filtered)

# Calculate the phase spectrum
phase_spectrum_original = np.angle(U_original)
phase_spectrum_filtered = np.angle(U_filtered)

# Calculate attenuation and phase shift
attenuation = amplitude_spectrum_filtered / amplitude_spectrum_original
phase_shift = phase_spectrum_filtered - phase_spectrum_original

# Plot the amplitude spectrum of original and filtered signals
plt.figure()
plt.stem(frequencies, amplitude_spectrum_original, label='Original Signal')
plt.stem(frequencies, amplitude_spectrum_filtered, label='Filtered Signal')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude')
plt.title('Amplitude Spectrum')
plt.legend()
plt.grid(True)

# Plot the phase spectrum of original and filtered signals
plt.figure()
plt.stem(frequencies, phase_spectrum_original, label='Original Signal')
plt.stem(frequencies, phase_spectrum_filtered, label='Filtered Signal')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Phase (radians)')
plt.title('Phase Spectrum')
plt.legend()
plt.grid(True)

# Plot attenuation and phase shift
plt.figure()
plt.stem(frequencies, attenuation)
plt.xlabel('Frequency (Hz)')
plt.ylabel('Attenuation')
plt.title('Signal Spectrum Components Attenuation')
plt.grid(True)

plt.figure()
plt.stem(frequencies, phase_shift)
plt.xlabel('Frequency (Hz)')
plt.ylabel('Phase Shift (radians)')
plt.title('Signal Spectrum Components Phase Shift')
plt.grid(True)

plt.show()

# Print the attenuation and phase shift values for reference
print("Attenuation:", attenuation)
print("Phase Shift:", phase_shift)