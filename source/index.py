from jinja2 import Undefined
from scipy.fft import irfft, rfft, rfftfreq
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

path_results = r'C:\Users\pjeiz\Project Makertron FHNW\FHNW-Makerton-Wega\XY_data\wrist_XY_01_filtered.csv'
raw_path = pd.read_csv(r'C:\Users\pjeiz\Project Makertron FHNW\FHNW-Makerton-Wega\XY_data\wrist_XY_01.csv')

def roundingFiter(df,decimals):
    print(df)
    df_rounded = df['Accelerometer X', 'Accelerometer Y', 'Accelerometer Z',].round(decimals)
    return df_rounded

def movingAverage(arr, window_size):
  
    arr['Accelerometer X'] = arr['Accelerometer X'].rolling(window_size).mean()
    arr['Accelerometer Y'] = arr['Accelerometer Y'].rolling(window_size).mean()
    arr['Accelerometer Z'] = arr['Accelerometer Z'].rolling(window_size).mean()
    
    
    # removing all the NULL values using
    # dropna() method
    arr.dropna(inplace=True)
    print(arr)
    
    return arr
"""
def fourierTransformAllAxies(raw_path, df):
    row_X = fourierTransform('X', df)
    row_Y = fourierTransform('Y', df)
    row_Z = fourierTransform('Z', df)
    
    row_X.columns = ['Accelerometer X']
    row_Y.columns = ['Accelerometer Y']
    row_Z.columns = ['Accelerometer Z']
    
    
    df_results = df[df.label == 14]
    print(row_X)
    print(df_results)
    df_results['Accelerometer X'] = row_X['Accelerometer X']
    df_results['Accelerometer Y'] = row_Y['Accelerometer Y']
    df_results['Accelerometer Z'] = row_Z['Accelerometer Z']
    
    return df_results

"""

def fourierTransform(axis, df, lowfilter=256, highfilter=0):
    
    df = df[df.label == 14]
    df = pd.DataFrame(df, columns= [f'Accelerometer {axis}']).to_numpy()
    
    
    yf = rfft(df)
    #yf = yf.astype(int)
    # Number of sample points
    N = len(df)
    # sample spacing
    fs = 256
    T = 1.0 / fs
    xf = rfftfreq(N, T)

    for index, x in enumerate(xf):
        if x >= lowfilter:
            yf[index] = 0
            
    for index, x in enumerate(xf):
        if x <= highfilter:
            yf[index] = 0
        


    plt.figure(figsize=(10,10))

    plt.plot(xf[:int(len(xf)*0.2)], np.abs(yf)[:int(len(xf)*0.2)])
    
    plt.title(f'Accelerometer {axis}')
    plt.xlabel('Frequency [Hz]')
    plt.ylabel('Volume [dBv]')

    plt.show()

    filtered_data = pd.DataFrame(irfft(yf, 1))
    
    return filtered_data


    
#fourierTransformAllAxies(raw_path, movingAverage(raw_path, 300)).to_csv(path_results, index=False)
row_X = fourierTransform('X', pd.DataFrame(raw_path))
print(row_X)
    
row_X.columns = ['Accelerometer X']
print(row_X)
    
    
df_results = pd.DataFrame(raw_path)[pd.DataFrame(raw_path).label == 14]
print(df_results)
df_results.columns = ['Accelerometer X']
df_results['Accelerometer X'] = row_X['Accelerometer X']
print(df_results)
