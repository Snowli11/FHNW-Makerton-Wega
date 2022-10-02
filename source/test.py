from scipy.fft import fft, fftfreq, irfft, rfft, rfftfreq
import numpy as np
import pandas as pd
from scipy.signal import butter, lfilter, freqz
import matplotlib.pyplot as plt
import csv

f = r'C:\Users\pjeiz\Project Makertron FHNW\FHNW-Makerton-Wega\XY_data\wrist_XY_01_filtered.csv'
raw_df = pd.read_csv(r'C:\Users\pjeiz\Project Makertron FHNW\FHNW-Makerton-Wega\XY_data\wrist_XY_01.csv')
print(raw_df)
df = pd.DataFrame(raw_df, columns= ['Accelerometer Z']).to_numpy()
print(df)

yf = rfft(df)
#yf = yf.astype(int)
print(yf)
# Number of sample points
N = len(df)
# sample spacing
fs = 256
T = 1.0 / fs
xf = rfftfreq(N, T)
xf_int = xf.astype(int)
print(len(xf))

xf_filtered = []

for index, x in enumerate(xf):
    if x >= 15:
        yf[index] = 0
    


plt.figure(figsize=(20,10))

plt.plot(xf[:int(len(xf)*0.2)], np.abs(yf)[:int(len(xf)*0.2)])

plt.show()



print(len(yf))


print(yf)

test = pd.DataFrame(irfft(yf, 1))

test.to_csv(f)