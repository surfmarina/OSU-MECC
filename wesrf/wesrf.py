from mhkit import wave
import matplotlib.pyplot as plt 
import datetime as dt
from mhkit import qc
import pandas as pd 
import numpy as np 
# JONSWAP AVERAGE SEA STATE
f = np.linspace(0.01,1,500)
Hs = 3
Tp = 4
S1 = wave.resource.jonswap_spectrum(f, Tp, Hs, gamma=3.3) 
S1.plot(xlabel='frequency [Hz]', ylabel = 'response[m^2/Hz]')
# elevation = mhkit.wave.resource.surface_elevation(S, time_index, seed=None, frequency_bins=None, phases=None)

# JONSWAP spectrum for creating short-term time-series - elevation profile for 20 minutes
t_st = 20.0 * 60.0

T_min = 1  # s
Tp = 8  # s
Hs = 1.5  # m
f0 = 1/t_st
f_max = 1/T_min
Nf = int(f_max/f0)
f = np.linspace(f0, f_max, Nf)
S2 = wave.resource.jonswap_spectrum(f, Tp, Hs)

# time in seconds
time = np.linspace(0, t_st, 2*Nf+1)
eta = wave.resource.surface_elevation(S2,time)
plt.plot(time,eta)

# Station 46002 (LLNR 765.1) - WEST OREGON - 275NM West of Coos Bay, OR
f = np.linspace(0.01,1,500)
Hs = 0.75
Tp = 2
S3 = wave.resource.pierson_moskowitz_spectrum(f, Tp, Hs)
S3.plot(xlabel='frequency [Hz]', ylabel = 'response[m^2/Hz]')

# Pierson Moskowitz spectrum for creating short-term time-series - elevation profile for 20 minutes
t_st = 20.0 * 60.0

T_min = 1  # s
Tp = 8  # s
Hs = 1.5  # m
f0 = 1/t_st
f_max = 1/T_min
Nf = int(f_max/f0)
f = np.linspace(f0, f_max, Nf)
S4 = wave.resource.pierson_moskowitz_spectrum(f, Tp, Hs)

# time in seconds
time = np.linspace(0, t_st, 2*Nf+1)
eta = wave.resource.surface_elevation(S4,time)
plt.plot(time,eta)
