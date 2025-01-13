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

