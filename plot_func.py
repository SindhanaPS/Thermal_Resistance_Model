import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
import matplotlib.ticker as tck
import math as m
from cmath import pi
from matplotlib.ticker import MultipleLocator

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
   ax1.set_xlim([2500,max(wpl2)])
   ax1.plot(wpllow1,dTlow1,linestyle='dashed',color='Orange')
   ax1.plot(wplhigh1,dThigh1,color='Orange',label=r'$\Gamma$=%.0fcm$^{-1}$' %eta1)
   ax1.plot(wpllow2,dTlow2,linestyle='dashed',color='red')
   ax1.plot(wplhigh2,dThigh2,color='red',label=r'$\Gamma$=%.0fcm$^{-1}$' %eta2)
   ax1.plot(wpllow3,dTlow3,linestyle='dashed',color='brown')
   ax1.plot(wplhigh3,dThigh3,color='brown',label=r'$\Gamma$=%.0fcm$^{-1}$' %eta3)

   plt.legend(fontsize="14")
   plt.savefig("figS20A.pdf",bbox_inches='tight',dpi=100)

def plotdTRVSC(wpl2, eta, wpllow, wplhigh, dTlow, dThigh, RVSClow, RVSChigh):
    fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True, figsize=(10, 8))

    plt.rcParams.update({
    'font.size': 24,
    })
 
    # Make the border of the plot bold
    for spine in ax1.spines.values():
       spine.set_linewidth(2)  # Adjust the border (spine) linewidth

    # Make the border of the plot bold
    for spine in ax2.spines.values():
       spine.set_linewidth(2)  # Adjust the border (spine) linewidth

    convfactor = 7.5 * 10**8
    RVSClow = RVSClow * convfactor
    RVSChigh = RVSChigh * convfactor
    Rinterlow = 8.94 * 10**5 * convfactor * np.ones_like(RVSClow)
    Rinterhigh = 8.94 * 10**5 * convfactor * np.ones_like(RVSChigh)
    
    # Plot for Delta T
    ax1.set_ylabel(r'-$\Delta$T ($\degree$C)', fontsize='26')
    ax1.plot(wpllow, dTlow, linestyle='dashed', color='limegreen', linewidth=4, label=r'$-\Delta$T$ low$')
    ax1.plot(wplhigh, dThigh, color='limegreen', linewidth=4, label=r'$-\Delta$T$ high$')
    ax1.tick_params(axis='both', which='major', labelsize=24, width=2)
 
    # Plot for Thermal resistance
    ax2.plot(wpllow, RVSClow, linestyle='dashed', linewidth=2, color='black')
    ax2.plot(wplhigh, RVSChigh, linewidth=4, color='black', label=r'$R_{VSC}$')
    ax2.plot(wpllow, Rinterlow, linewidth=4, color='lightgrey', label=r'$R_{inter}$')
    ax2.plot(wplhigh, Rinterhigh, linewidth=4, color='lightgrey')
    ax2.set_ylabel('Thermal\nresistance (K/W)', fontsize='24')
    ax2.legend(loc='upper left', fontsize="24")
    ax2.set_xlim([2500, max(wpl2)])
    ax2.tick_params(axis='both', which='major', labelsize=24, width=2)

    # Shared X-axis label
    plt.xlabel(r'$\omega_{pl}$ (cm$^{-1}$)', fontsize='24')
    
    plt.tight_layout()
    plt.savefig("figS21A.pdf",bbox_inches='tight',dpi=100)

def plotdTR(wpl2,R1,R2,R3,R4,wpllow,wplhigh,dTlow1,dThigh1,dTlow2,dThigh2,dTlow3,dThigh3,dTlow4,dThigh4):
   fig,ax1 = plt.subplots()
   plt.ylabel(r'-$\Delta$T ($\degree$C)')
   plt.xlabel(r'$\omega_{pl}$ (cm$^{-1}$)')

   ax1.set_ylim([0,15])
   ax1.set_xlim([2500,max(wpl2)])
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
   plt.savefig("figS20B.pdf",bbox_inches='tight',dpi=100)

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

def plotTonsetRVSC(wpl2, eta2, wpllow, wplhigh, Tplatelow, Tplatehigh, RVSClow, RVSChigh, wplResonant, wplControl, TplateResonant, TplateControl):
   ######################################################
   #                 Formatting                         #
   ######################################################


    plt.rcParams.update({
    'font.size': 26,
    'font.family': 'Arial',
    'font.weight': 'bold'
    })

    convfactor = 7.5 * 10**8
    RVSClow = RVSClow * convfactor
    RVSChigh = RVSChigh * convfactor
    Rinterlow = 8.94 * 10**5 * convfactor * np.ones_like(RVSClow)
    Rinterhigh = 8.94 * 10**5 * convfactor * np.ones_like(RVSChigh)

    # Create a single subplot with specified aspect ratio
    fig, ax = plt.subplots(figsize=(8, 6))  # Width is 1.5 times the total height
    
    # Make the border of the plot bold
    for spine in ax.spines.values():
       spine.set_linewidth(3)  # Adjust the border (spine) linewidth

    ax.tick_params(axis='both', which='major', labelsize=26, width=3, direction='in', length=7)
    
    # Plot 'dTlow' and 'dThigh' on the subplot
    ax.plot(wpllow, Tplatelow, linestyle='dashed', color='black', linewidth=3)
    ax.plot(wplhigh, Tplatehigh, color='black', linewidth=3)
    ax.plot(wplResonant, TplateResonant, color='#0072BD',marker='s',markersize=15)
    ax.plot(wplControl, TplateControl, color='#D95319',marker='s',markersize=15)
    ax.set_xlabel(r'$\mathbf{\omega_{pl}}$ (cm$\mathbf{^{-1}}$)', fontweight='bold', fontsize='30')
    ax.set_ylabel(r'Onset T. ($\degree$C)', fontweight='bold', fontsize='30')

    ax.set_xlim([2500, max(wpl2)])
    ax.yaxis.set_major_locator(MultipleLocator(1))
    # Add grey grid lines parallel to the x-axis
    ax.grid(which='both', axis='y', linestyle='-', linewidth=3, color='lightgray')

    # Adjust the layout to prevent overlapping
    plt.tight_layout()

    # Save the plot as a PDF
    fig.savefig("fig5D.pdf", bbox_inches='tight', dpi=100)
