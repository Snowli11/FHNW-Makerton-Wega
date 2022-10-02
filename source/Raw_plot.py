from scipy.fft import fft, fftfreq, irfft, rfft, rfftfreq
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

raw_path = pd.read_csv(r'C:\Users\pjeiz\Project Makertron FHNW\FHNW-Makerton-Wega\XY_data\wrist_XY_02.csv')
raw_path = raw_path#[raw_path.label == 14]

df = pd.DataFrame(raw_path)



df['Accelerometer X'] = df['Accelerometer X'].rolling(1000).mean()
df.dropna(inplace=True) 



df.plot(kind='line', x='Timestamp UTC', y='Accelerometer X')
plt.subplot

plt.show()