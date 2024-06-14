import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
import matplotlib.ticker as tck
import math as m
from cmath import pi

def plotkoverdw(wpl,eta1,eta2,eta3,ratLP1,ratUP1,ratLP2,ratUP2,ratLP3,ratUP3,w1,w2,w3):
   fig,ax1 = plt.subplots()
   plt.ylabel(r'$k_{i\to j}^*/|\omega_i-\omega_j|$')
   plt.xlabel(r'$\omega_{pl}^*$')
   
   ax1.set_ylim([0,2])
   ax1.plot(wpl,ratLP1,label=r'$k_{LP\to D}^*/|\omega_{vm}^*-\omega_{LP}^*|$ for $\eta^*$=%.2f' %eta1,linewidth=2)
   ax1.plot(wpl,ratUP1,label=r'$k_{UP\to D}^*/|\omega_{UP}^*-\omega_{vm}^*|$ for $\eta^*$=%.2f' %eta1,linewidth=2)
   ax1.plot(wpl,ratLP2,label=r'$k_{LP\to D}^*/|\omega_{vm}^*-\omega_{LP}^*|$ for $\eta^*$=%.2f' %eta2,linewidth=2)
   ax1.plot(wpl,ratUP2,label=r'$k_{UP\to D}^*/|\omega_{UP}^*-\omega_{vm}^*|$ for $\eta^*$=%.2f' %eta2,linewidth=2)
   ax1.plot(wpl,ratLP3,label=r'$k_{LP\to D}^*/|\omega_{vm}^*-\omega_{LP}^*|$ for $\eta^*$=%.2f' %eta3,linewidth=2)
   ax1.plot(wpl,ratUP3,label=r'$k_{UP\to D}^*/|\omega_{UP}^*-\omega_{vm}^*|$ for $\eta^*$=%.2f' %eta3,linewidth=2)

   plt.vlines(x = w1, color = 'Black', linestyle='dashed', ymax=1, ymin=0)
   plt.vlines(x = w2, color = 'Black', linestyle='dashed', ymax=1, ymin=0)
   plt.vlines(x = w3, color = 'Black', linestyle='dashed', ymax=1, ymin=0)
   plt.axhline(y = 1, color = 'Black', linestyle='dashed')

   plt.legend(fontsize="8")

   plt.savefig("rate_constant_dw.pdf",bbox_inches='tight',dpi=100)

def plotdTeta(wpl2,eta1,eta2,eta3,wpllow1,wplhigh1,wpllow2,wplhigh2,wpllow3,wplhigh3,dTlow1,dThigh1,dTlow2,dThigh2,dTlow3,dThigh3):
   fig,ax1 = plt.subplots()
   plt.ylabel(r'-$\Delta$T ($\degree$C)')
   plt.xlabel(r'$\omega_{pl}$ (cm$^{-1}$)')

   convfactor = 3242
   eta1 = eta1*convfactor
   eta2 = eta2*convfactor
   eta3 = eta3*convfactor

   ax1.set_ylim([0,15])
   ax1.set_xlim([min(wpl2),max(wpl2)])
   ax1.plot(wpllow1,dTlow1,linestyle='dashed',color='Orange')
   ax1.plot(wplhigh1,dThigh1,color='Orange',label=r'$\Gamma$=%.0fcm$^{-1}$' %eta1)
   ax1.plot(wpllow2,dTlow2,linestyle='dashed',color='red')
   ax1.plot(wplhigh2,dThigh2,color='red',label=r'$\Gamma$=%.0fcm$^{-1}$' %eta2)
   ax1.plot(wpllow3,dTlow3,linestyle='dashed',color='brown')
   ax1.plot(wplhigh3,dThigh3,color='brown',label=r'$\Gamma$=%.0fcm$^{-1}$' %eta3)

   plt.legend(fontsize="14")
   plt.savefig("figS2A.pdf",bbox_inches='tight',dpi=100)

def plotdTRVSC(wpl2,eta,wpllow,wplhigh,dTlow,dThigh,R):
   fig,ax1 = plt.subplots()
   plt.xlabel(r'$\omega_{pl}$ (cm$^{-1}$)')

   convfactor = 7.5*10**8
   R = R*convfactor
   Rinter = 8.94*10**5*convfactor*np.ones_like(R)
   ax1.set_ylim([0,15])
   ax1.set_ylabel(r'-$\Delta$T ($\degree$C)')
   ax1.set_xlim([min(wpl2),max(wpl2)])
   ax1.plot(wpllow,dTlow,linestyle='dashed',color='limegreen',linewidth=2)
   ax1.plot(wplhigh,dThigh,color='limegreen',linewidth=2,label=r'$-\Delta$T')
   ax1.yaxis.label.set_color('limegreen')
   ax1.tick_params(axis='y', colors='limegreen')
   plt.legend(fontsize="14")
   ax2 = ax1.twinx()
   ax2.plot(wpl2,R,linewidth=2,color='black',label=r'$R_{VSC}$')
   ax2.plot(wpl2,Rinter,linewidth=2,color='lightgrey',label=r'$R_{inter}$')
   ax2.set_ylabel('Thermal resistance (K/W)')
   ax1.spines['left'].set_color('limegreen')

   plt.legend(fontsize="14")
   plt.savefig("figS3.pdf",bbox_inches='tight',dpi=100)

def plotdTR(wpl2,R1,R2,R3,R4,wpllow,wplhigh,dTlow1,dThigh1,dTlow2,dThigh2,dTlow3,dThigh3,dTlow4,dThigh4):
   fig,ax1 = plt.subplots()
   plt.ylabel(r'-$\Delta$T ($\degree$C)')
   plt.xlabel(r'$\omega_{pl}$ (cm$^{-1}$)')

   ax1.set_ylim([0,15])
   ax1.set_xlim([min(wpl2),max(wpl2)])
   ax1.plot(wpllow,dTlow1,linestyle='dashed',color='cyan')
   #ax1.plot(wplhigh,dThigh1,color='cyan',label='$R^*_{total}$=%.2E' %R1)
   ax1.plot(wplhigh,dThigh1,color='cyan',label=r'$R_{tot}=7.5\times10^{13}K/W$')
   ax1.plot(wpllow,dTlow2,linestyle='dashed',color='deepskyblue')
   #ax1.plot(wplhigh,dThigh2,color='deepskyblue',label='$R^*_{total}$=%.2E' %R2)
   ax1.plot(wplhigh,dThigh2,color='deepskyblue',label=r'$R_{tot}=7.5\times10^{14}K/W$')
   ax1.plot(wpllow,dTlow3,linestyle='dashed',color='blue')
   #ax1.plot(wplhigh,dThigh3,color='blue',label='$R^*_{total}$=%.2E' %R3)
   ax1.plot(wplhigh,dThigh3,color='blue',label=r'$R_{tot}=7.5\times10^{15}K/W$')
   ax1.plot(wpllow,dTlow4,linestyle='dashed',color='navy')
   #ax1.plot(wplhigh,dThigh4,color='navy',label='$R^*_{total}$=%.2E' %R4)
   ax1.plot(wplhigh,dThigh4,color='navy',label=r'$R_{tot}=7.5\times10^{16}K/W$')

   plt.legend(fontsize="14",loc='upper right')
   plt.savefig("figS2B.pdf",bbox_inches='tight',dpi=100)

def plotThermalProfile(Tair,TplControl,TmolControl,TplateControl,TplResonant,TmolResonant,TplateResonant,dAu,dAl2O3,dinter,dCuSO4,ratAu,ratAl2O3):
   fig,ax1 = plt.subplots(figsize=(8, 2.5))
   plt.ylabel(r'T ($\degree$C)')
   plt.xlabel(r'd (nm)')

   TAl2O3c = TplateControl + (TplControl - TplateControl)*ratAu/(ratAu+ratAl2O3)
   TAl2O3r = TplateResonant + (TplResonant - TplateResonant)*ratAu/(ratAu+ratAl2O3)

#   ax1.set_ylim([0,50])
   Tcontrol = [TplateControl,TAl2O3c,TplControl,TmolControl,Tair]
   Tresonant = [TplateResonant,TAl2O3r,TplResonant,TmolResonant,Tair]
   d = [0,dAu,dAu+dAl2O3,dAu+dAl2O3+dinter,dAu+dAl2O3+dinter+dCuSO4]

   ax1.set_xlim(0,max(d))
   ax1.plot(d,Tresonant,color='#FFC107',label='resonant')
   ax1.plot(d,Tcontrol,color='black',linestyle='dashed',label='control')

   plt.legend(fontsize="14",loc='upper right')
   plt.savefig("figS21B.pdf",bbox_inches='tight',dpi=100)
