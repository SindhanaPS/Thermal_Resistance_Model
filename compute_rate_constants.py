import numpy as np
from spectral_func import *

wvmt = 3242      # All frequencies are in scaled with this frequency

# Debye spectral density parameters
wc = 500/wvmt
eta = 0.08
filename = 'rate_const_0_08.txt'

# Other parameters
wvm = 3242/wvmt
g0 = 222/wvmt
gammapl = 243/wvmt
gammavm = 252/wvmt

N = 10**6

# Transition temperature is 309K which equals 36 deg C
Ttrns = 309*(1.38*10**(-23))/(6.626*10**(-34)*2.99*10**(10)*wvmt)

# Minimum and maximum values of wpl
wpllow = (max(gammapl,gammavm)/(2*g0))**(2/3)
wplhigh = (0.1/g0)**(2/3)

# Plasmon frequency
wpl = np.linspace(wpllow,wplhigh,num=100)

# Light-matter coupling strength
gpl = gwpl(wpl,g0)

# Rate constants and gaps
kLP,kUP,dwLP,dwUP = kLPUPtoD(N,wpl,wvm,g0,Ttrns,wc,eta)

# Save output to a file
np.savetxt(filename,(wpl,gpl,kLP,kUP,dwLP,dwUP))
