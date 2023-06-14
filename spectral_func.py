import numpy as np
import cmath as cm
import math as m
from cmath import pi

# All variables are rescaled and dimensionless

def gwpl(wpl,g0):
   gw = g0*np.power(wpl,3/2)
   return gw

def Rabi(wpl,wvm,g0):
   delta = wpl - wvm
   gw = gwpl(wpl,g0)
   Omega = np.sqrt(4*np.square(gw)+np.square(delta))
   return (Omega)

def Polfreq(wpl,wvm,g0):
   delta = wpl - wvm
   Omega = Rabi(wpl,wvm,g0)
   wLP = wvm + (delta - Omega)/2 
   wUP = wvm + (delta + Omega)/2 
   return (wLP,wUP)

def JDebye(w,wc,eta):
   J = eta*wc*np.divide(w,wc**2+np.square(w))
   return (J)

def nT(w,T):
   n = np.divide(1,np.exp(w/T)-1)
   return (n)

def HopfieldSquared(wpl,wvm,g0):
   delta = wpl - wvm
   Omega = Rabi(wpl,wvm,g0)

   sLPpl = np.divide(Omega-delta,2*Omega) 
   sLPvm = np.divide(Omega+delta,2*Omega) 
   sUPpl = np.divide(Omega+delta,2*Omega) 
   sUPvm = np.divide(Omega-delta,2*Omega) 

   return (sLPvm,sLPpl,sUPvm,sUPpl)

def kLPUPtoD(N,wpl,wvm,g0,Ttrns,wc,eta):
   # Polariton frequencies
   wLP,wUP = Polfreq(wpl,wvm,g0)

   # Difference in frequency between polariton and dark modes
   dwUP = wUP - wvm
   dwLP = wvm - wLP
   
   # Occupation number
   nphUP = nT(dwUP,Ttrns)
   nphLP = nT(dwLP,Ttrns)

   # Hopfield coefficients squared
   sLPvm,sLPpl,sUPvm,sUPplv = HopfieldSquared(wpl,wvm,g0)

   # Spectral density
   JUP = JDebye(dwUP,wc,eta)
   JLP = JDebye(dwLP,wc,eta)

   kUP = ((N-1)/N)*np.multiply(sUPvm, np.multiply(JUP, nphUP+1))
   kLP = ((N-1)/N)*np.multiply(sLPvm, np.multiply(JLP, nphLP))

   return (kLP,kUP,dwLP,dwUP)
