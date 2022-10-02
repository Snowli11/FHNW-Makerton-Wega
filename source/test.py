from scipy.fft import fft, fftfreq, irfft, rfft, rfftfreq
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

path_results = r'C:\Users\pjeiz\Project Makertron FHNW\FHNW-Makerton-Wega\XY_data\wrist_XY_01_filtered.csv'
raw_path = pd.read_csv(r'C:\Users\pjeiz\Project Makertron FHNW\FHNW-Makerton-Wega\XY_data\wrist_XY_01.csv')

def fourierTransformAllAxies(raw_path):
    row_X = fourierTransform('X', raw_path)
    row_Y = fourierTransform('Y', raw_path)
    row_Z = fourierTransform('Z', raw_path)
    
    row_X.columns = ['Accelerometer X']
    row_Y.columns = ['Accelerometer Y']
    row_Z.columns = ['Accelerometer Z']
    
    df_results = raw_path
    print(df_results)
    df_results['Accelerometer X'] = row_X['Accelerometer X']
    df_results['Accelerometer Y'] = row_Y['Accelerometer Y']
    df_results['Accelerometer Z'] = row_Z['Accelerometer Z']
    
    return df_results

def fourierTransform(axis, raw_path, lowfilter=256):
    df = pd.DataFrame(raw_path, columns= [f'Accelerometer {axis}']).to_numpy()
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
        if x >= lowfilter:
            yf[index] = 0
        


    plt.figure(figsize=(10,10))

    plt.plot(xf[:int(len(xf)*0.2)], np.abs(yf)[:int(len(xf)*0.2)])
    
    plt.title(f'Accelerometer {axis}')
    plt.xlabel('Frequency [Hz]')
    plt.ylabel('Volume [dBv]')

    plt.show()



    print(len(yf))


    print(yf)

    filtered_data = pd.DataFrame(irfft(yf, 1))
    
    return filtered_data


    
fourierTransformAllAxies(raw_path).to_csv(path_results, index=False)