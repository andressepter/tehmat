import sys; sys.path.append('/home/asepter/.local/lib/python3.10/site-packages/')
import galois as galois
import numpy as np

import numpy as np

# Define the periodic signal u
u = np.array([1, -1, 0, 0, -1, 1])

# Calculate the DFT of the signal
U = np.fft.fft(u)

# Print the DFT result
print("DFT of the signal u:", U)

# Define the signal u where u values are the absolute value of n^2 and n is between 0 and 4
n = np.arange(5)
u = np.abs(n**2)

# Calculate the Fourier Transform of the signal
U = np.fft.fft(u)

# Print the Fourier Transform result
print("Fourier Transform of the signal u:", U)

import numpy as np

# Define the period N
N = 8

# Define the signal u where u values are Sin(Pi*n/4 + Pi/8) and n is between 0 and N-1
n = np.arange(N)
u = np.sin(np.pi * n / 4 + np.pi / 8)

# Calculate the Fourier Transform of the signal
U = np.fft.fft(u)

# Print the Fourier Transform result
print("Fourier Transform of the signal u:", U)

# Define the period N
N = 8

# Define the signal u where u values are Sin(Pi*n/4 + Pi/8) and n is between 0 and N-1
n = np.arange(N)
u = np.sin(np.pi * n / 4 + np.pi / 8)

# Calculate the Fourier Transform of the signal
U = np.fft.fft(u)

# Function to plot the amplitude spectrum with lines connecting the dots
def plot_amplitude_spectrum(U):
    N = len(U)
    n = np.arange(N)
    T = N / 1.0
    freq = n / T 

    plt.plot(freq, np.abs(U), 'b-o')  # Use plot instead of stem to connect the dots
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Amplitude |U(freq)|')
    plt.title('Amplitude Spectrum')
    plt.grid(True)
    plt.show()

# Function to plot the phase spectrum with lines connecting the dots
def plot_phase_spectrum(U):
    N = len(U)
    n = np.arange(N)
    T = N / 1.0
    freq = n / T 

    plt.plot(freq, np.angle(U), 'b-o')  # Use plot instead of stem to connect the dots
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Phase (radians)')
    plt.title('Phase Spectrum')
    plt.grid(True)
    plt.show()

# Print the Fourier Transform result
print("Fourier Transform of the signal u:", U)

# Plot the amplitude spectrum
plot_amplitude_spectrum(U)

# Plot the phase spectrum
plot_phase_spectrum(U)

#Reverse DFT
# Define the period N
N = 8

# Define the DFT values of the signal
U = np.array([3, 5, -0.5 + 1.20710678j, -0.5 + 0.5j, -0.5 + 0.20710678j, -0.5, 0, 0])

# Calculate the inverse DFT to get the original signal
u = np.fft.ifft(U)

# Calculate (u * u)[0]
result = (u * u)[0]

# Print the result
print("Result of (u * u)[0]:", result)

#vektorite korrutamine
 Define the vectors u and h
u = np.array([n/4 if 0 <= n <= 4 else 0 for n in range(8)])
h = np.array([1/2 if n == 0 else -1/2 if n == 1 else 0 for n in range(8)])

# Multiply the vectors u and h
result = u * h

# Print the result
print("Result of multiplying vectors u and h:", result)

#konvolutsioon
# Define the vectors u and h
u = np.array([n/4 if 0 <= n <= 4 else 0 for n in range(8)])
h = np.array([1/2 if n == 0 else -1/2 if n == 1 else 0 for n in range(8)])

# Calculate the convolution of u and h
convolution_result = np.convolve(u, h, mode='full')

# Print the result
print("Convolution of vectors u and h:", convolution_result)

#continous signal u(t)=3sin(2+Pi+t) - 2sin(4 * pi * t). Plot graph. Plot sampled signal grap Signal is sampled  10 Hz, 15, 20 Hz. Calculate attenuation and phase shift. Convolution filter parameters are h=(1/2,1/2) and h=(1/5,1/5,1/5,1/5,1/5). Plot filtered signal graph. 

import numpy as np
import matplotlib.pyplot as plt

# Define the continuous signal u(t)
def u(t):
    return 3 * np.sin(2 + np.pi + t) - 2 * np.sin(4 * np.pi * t)

# Define the time range for the continuous signal
t = np.linspace(0, 1, 1000)

# Plot the continuous signal
plt.figure(figsize=(12, 6))
plt.plot(t, u(t), label='Continuous Signal')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Continuous Signal u(t) = 3sin(2+Pi+t) - 2sin(4 * pi * t)')
plt.legend()
plt.grid(True)
plt.show()

# Define the sampling frequencies
sampling_frequencies = [10, 15, 20]

# Plot the sampled signals
plt.figure(figsize=(12, 6))
for fs in sampling_frequencies:
    ts = np.arange(0, 1, 1/fs)
    us = u(ts)
    plt.plot(ts, us, marker='o', linestyle='-', label=f'Sampled Signal at {fs} Hz')

plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Sampled Signals at Different Frequencies')
plt.legend()
plt.grid(True)
plt.show()

# Define the convolution filters
h1 = np.array([1/2, 1/2])
h2 = np.array([1/5, 1/5, 1/5, 1/5, 1/5])

# Plot the filtered signals for each sampling frequency and filter
for fs in sampling_frequencies:
    ts = np.arange(0, 1, 1/fs)
    us = u(ts)
    
    # Filter with h1
    filtered_signal_h1 = np.convolve(us, h1, mode='same')
    
    # Filter with h2
    filtered_signal_h2 = np.convolve(us, h2, mode='same')
    
    plt.figure(figsize=(12, 6))
    plt.plot(ts, us, marker='o', linestyle='-', label=f'Sampled Signal at {fs} Hz')
    plt.plot(ts, filtered_signal_h1, marker='x', linestyle='-', label=f'Filtered Signal with h=(1/2,1/2)')
    plt.plot(ts, filtered_signal_h2, marker='s', linestyle='-', label=f'Filtered Signal with h=(1/5,1/5,1/5,1/5,1/5)')
    
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.title(f'Filtered Signals at {fs} Hz Sampling Frequency')
    plt.legend()
    plt.grid(True)
    plt.show()

# Calculate attenuation and phase shift for each sampling frequency and filter
def calculate_attenuation_phase_shift(original_signal, filtered_signal):
    attenuation = np.abs(filtered_signal) / np.abs(original_signal)
    phase_shift = np.angle(filtered_signal) - np.angle(original_signal)
    return attenuation, phase_shift

for fs in sampling_frequencies:
    ts = np.arange(0, 1, 1/fs)
    us = u(ts)
    
    # Filter with h1
    filtered_signal_h1 = np.convolve(us, h1, mode='same')
    
    # Filter with h2
    filtered_signal_h2 = np.convolve(us, h2, mode='same')
    
    # Calculate attenuation and phase shift for h1
    attenuation_h1, phase_shift_h1 = calculate_attenuation_phase_shift(us, filtered_signal_h1)
    
    # Calculate attenuation and phase shift for h2
    attenuation_h2, phase_shift_h2 = calculate_attenuation_phase_shift(us, filtered_signal_h2)
    
    print(f"Sampling Frequency: {fs} Hz")
    print(f"Filter h=(1/2,1/2): Attenuation: {attenuation_h1}, Phase Shift: {phase_shift_h1}")
    print(f"Filter h=(1/5,1/5,1/5,1/5,1/5): Attenuation: {attenuation_h2}, Phase Shift: {phase_shift_h2}")

