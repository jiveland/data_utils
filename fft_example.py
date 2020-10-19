# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 16:58:17 2020

@author: jiveland
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
import scipy.fftpack

#example df from csv
df = pd.read_csv('./path/df.csv')

amp = df['Y'].values
##return fft
amp_fft = sp.fftpack.fft(amp)
##return fft^2
amp_psd = np.abs(amp_fft)**2
fftfreq = sp.ftpack.fftfreq(len(amp_fft),1/1.25)
#here 1.25 is an example time spacing in the data
i = fftfreq > 0
fig,ax = plt.subplots(1,1,figsize(8,4))
ax.plot(fftfreq[i],amp_psd[i])
ax.set_xlim(0,.1)
ax.set_xlabel('FREQ')
ax.set_ylabel('PSD')
plt.show()

#next plot on a log scale
fig,ax = plt.subplots(1,1,figsize(8,4))
ax.plot(fftfreq[i],10*np.log10(amp_psd[i]))
ax.set_xlim(0,.3)
ax.set_xlabel('FREQ')
ax.set_ylabel('PSD (dB)')
plt.show()

##invert to compare to original

amp_fft_bis = amp_fft.copy()
#apply a band pass filter to exclude high and low frequencies in the inverse
amp_fft_bis[(np.abs(fftfreq)>.06)|(np.abs(fftfreq)<0.04)]=0
amp_slow = np.real(sp.fftpack.ifft(amp_fft_bis))
fig,ax = plt.subplots(1,1,figsize=(8,4))
#plot origianl data along with fft inverse
ax.plot(df['1/FREQ'],amp_slow)
#shift inverse data down to 0 if needed
axplot(df['1/FREQ'],amp-amp.mean())
ax.set_xlim(0,300)
ax.setxlabel('1/f')
ax.set_ylabel('intensity A.U.')
plt.show()
