from scipy.fft import fft, ifft
import numpy as np
import matplotlib.pyplot as plt
x = np.array([1.0, 2.0, 1.0, -1.0, 1.5])
y = fft(x)
N = 600
# sample spacing
T = 1.0 / 800.0
xf = fftfreq(N, T)[:N//2]
plt.plot(, 2.0/N * np.abs(yf[0:N//2]))
plt.grid()
plt.show()

print(y)
