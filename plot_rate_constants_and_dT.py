import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter
import numpy as np
from matplotlib import rc
from matplotlib import rcParams
from spectral_func import *
from plot_func import *


wvm = 3242

# All distances in nm
dAu = 200
dAl2O3 = 40
dinter = 10
dCuSO4 = 1000

# Ratio of temperature drop over Au and Al2O3
ratAu = 0.63
ratAl2O3 = 1.33

Tair = 25 

#####################################################
#                Importing data                     #
#####################################################

wpl,gpl,kLP1,kUP1,dwLP1,dwUP1 = np.loadtxt('rate_const_0_02.txt')
wpl,gpl,kLP2,kUP2,dwLP2,dwUP2 = np.loadtxt('rate_const_0_04.txt')
wpl,gpl,kLP3,kUP3,dwLP3,dwUP3 = np.loadtxt('rate_const_0_08.txt')
data1 = np.loadtxt('deltaT_eta_0_02.dat')
data2 = np.loadtxt('deltaT_eta_0_04.dat')
data3 = np.loadtxt('deltaT_eta_0_08.dat')
data4 = np.loadtxt('deltaT_R_5.dat')
data5 = np.loadtxt('deltaT_R_6.dat')
data6 = np.loadtxt('deltaT_R_7.dat')
data7 = np.loadtxt('deltaT_R_8.dat')

delta = data1[:,0]
wpl2 = data1[:,1]
dT1 = data1[:,3]
dT2 = data2[:,3]
dT3 = data3[:,3]

Tplate2 = data2[:,2]
Q2 = data2[:,5]
Tpl2 = data2[:,7]
Tmol2 = data2[:,8]
RVSC2 = np.divide(Tpl2-Tmol2,Q2)

wpl3 = data4[:,1]
dT4 = data4[:,3]
dT5 = data5[:,3]
dT6 = data6[:,3]
dT7 = data7[:,3]

eta1 = 0.02
eta2 = 0.04
eta3 = 0.08

R1=10**(5)
R2=10**(6)
R3=10**(7)
R4=10**(8)

ratLP1 = np.divide(kLP1,dwLP1)
ratUP1 = np.divide(kUP1,dwUP1)
ratLP2 = np.divide(kLP2,dwLP2)
ratUP2 = np.divide(kUP2,dwUP2)
ratLP3 = np.divide(kLP3,dwLP3)
ratUP3 = np.divide(kUP3,dwUP3)


for i in range(wpl.size-1):
   if ratUP1[i]>1 and ratUP1[i+1]<=1:
      w1 = wpl[i] 
   if ratUP2[i]>1 and ratUP2[i+1]<=1:
      w2 = wpl[i]
   if ratUP3[i]>1 and ratUP3[i+1]<=1:
      w3 = wpl[i]

print(w1,w2,w3)

w1r=w1*wvm
w2r=w2*wvm
w3r=w3*wvm

# Divide each dT array into two parts eta
for i in range(wpl2.size-1):
   if wpl2[i]<w1r and wpl2[i+1]>=w1r:
      wpllow1 = wpl2[:i+2]
      wplhigh1 = wpl2[i+1:]
      dTlow1 = dT1[:i+2]
      dThigh1 = dT1[i+1:]
   if wpl2[i]<w2r and wpl2[i+1]>=w2r:
      wpllow2 = wpl2[:i+2]
      wplhigh2 = wpl2[i+1:]
      dTlow2 = dT2[:i+2]
      dThigh2 = dT2[i+1:]
      RVSClow2 = RVSC2[:i+2]
      RVSChigh2 = RVSC2[i+1:]
      Tplatelow2 = Tplate2[:i+2]
      Tplatehigh2 = Tplate2[i+1:]
   if wpl2[i]<w3r and wpl2[i+1]>=w3r:
      wpllow3 = wpl2[:i+2]
      wplhigh3 = wpl2[i+1:]
      dTlow3 = dT3[:i+2]
      dThigh3 = dT3[i+1:]

# Divide each dT array into two parts R
for i in range(wpl3.size-1):
   if wpl3[i]<w2r and wpl3[i+1]>=w2r:
      wpllow = wpl3[:i+2]
      wplhigh = wpl3[i+1:]
      dTlow4 = dT4[:i+2]
      dThigh4 = dT4[i+1:]
      dTlow5 = dT5[:i+2]
      dThigh5 = dT5[i+1:]
      dTlow6 = dT6[:i+2]
      dThigh6 = dT6[i+1:]
      dTlow7 = dT7[:i+2]
      dThigh7 = dT7[i+1:]

# Collect Tpl, Tmol, Tstage at resonance wpl=wvm and at wpl=4000cm^-1 in degree celsius
### wpl = 40000cm^-1
wplControl=4000
for i in range(wpl2.size-1):
   if wpl2[i]<wplControl and wpl2[i+1]>=wplControl:
      TplControl = Tpl2[i+1]*6.626*10**(-34)*2.99*10**(10)*3242/(1.38*10**(-23)) - 273
      TmolControl = Tmol2[i+1]*6.626*10**(-34)*2.99*10**(10)*3242/(1.38*10**(-23)) - 273
      TplateControl = Tplate2[i+1]

### wpl = wvm
wplResonant = wvm
for i in range(wpl2.size-1):
   if wpl2[i]<wplResonant and wpl2[i+1]>=wplResonant:
      TplResonant = Tpl2[i+1]*6.626*10**(-34)*2.99*10**(10)*3242/(1.38*10**(-23)) - 273
      TmolResonant = Tmol2[i+1]*6.626*10**(-34)*2.99*10**(10)*3242/(1.38*10**(-23)) - 273
      TplateResonant = Tplate2[i+1]

######################################################
#                 Formatting                         #
######################################################

font = {
        'weight' : 'normal',
        'size'   : 16}

plt.rc('font', **font)

# Set additional rc parameters
rcParams['mathtext.fontset'] = 'cm'
rcParams['text.latex.preamble'] = r'\usepackage{physics} \usepackage{amsmath} \usepackage{gensymb}'

######################################################
#                 Plotting                           #
######################################################

plotkoverdw(wpl,eta1,eta2,eta3,ratLP1,ratUP1,ratLP2,ratUP2,ratLP3,ratUP3,w1,w2,w3)

plotdTeta(wpl2,eta1,eta2,eta3,wpllow1,wplhigh1,wpllow2,wplhigh2,wpllow3,wplhigh3,dTlow1,dThigh1,dTlow2,dThigh2,dTlow3,dThigh3)

plotdTR(wpl3,R1,R2,R3,R4,wpllow,wplhigh,dTlow4,dThigh4,dTlow5,dThigh5,dTlow6,dThigh6,dTlow7,dThigh7)

plotThermalProfile(Tair,TplControl,TmolControl,TplateControl,TplResonant,TmolResonant,TplateResonant,dAu,dAl2O3,dinter,dCuSO4,ratAu,ratAl2O3)

plotdTRVSC(wpl2,eta2,wpllow2,wplhigh2,dTlow2,dThigh2,RVSClow2,RVSChigh2)

plotdTRVSC2(wpl2,eta2,wpllow2,wplhigh2,dTlow2,dThigh2,RVSClow2,RVSChigh2)

plotdTeta2(wpl2,eta1,eta2,eta3,wpllow1,wplhigh1,wpllow2,wplhigh2,wpllow3,wplhigh3,dTlow1,dThigh1,dTlow2,dThigh2,dTlow3,dThigh3)

plotdTR2(wpl3,R1,R2,R3,R4,wpllow,wplhigh,dTlow4,dThigh4,dTlow5,dThigh5,dTlow6,dThigh6,dTlow7,dThigh7)

plotTonsetRVSC(wpl2,eta2,wpllow2,wplhigh2,Tplatelow2,Tplatehigh2,RVSClow2,RVSChigh2,wplResonant,wplControl,TplateResonant,TplateControl)
