from scipy.fft import fft, fftfreq, rfft, rfftfreq
import numpy as np
import pandas as pd

import plotly.plotly as py
import plotly.graph_objs as go
import plotly.figure_factory as ff

raw_df = pd.read_csv(r'C:\Users\pjeiz\Project Makertron FHNW\FHNW-Makerton-Wega\XY_data\wrist_XY_01.csv')
rslt_df = raw_df[raw_df['label'] == 14]
print(rslt_df)
df = pd.DataFrame(rslt_df, columns= ['Accelerometer X']).to_numpy()
print(df)

yf = rfft(df)
print(yf)
# Number of sample points
N = len(df)
# sample spacing
T = 1.0 / 256
xf = rfftfreq(N, T)
print(xf)

fig = go.Figure([go.Scatter(x=xf['Frequency'], y=yf['Amplitude'])])
fig.show()
