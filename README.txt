######################################################################################################
Code accompanying manuscript https://www.nature.com/articles/s41557-024-01723-6

Everything is in reduced units in the mathematica notebook 'heat_flow_with_polaritons_mechanism.nb'

The code 'heat_flow_with_polaritons_mechanism.nb' with:

1) R_{total}=1.6*10^6 and \eta=0.02,0.04,0.08 can generate data for Figure S25A.
   We name these files: deltaT_eta_0_02.dat, deltaT_eta_0_04.dat, and deltaT_eta_0_08.dat
1) R_{total}=10^5,10^6,10^7,10^8 and \eta=0.04 can generate data for Figure S25B.
   We name these files: deltaT_R_5.dat, deltaT_R_6.dat, deltaT_R_7.dat, and deltaT_R_8.dat
3) R_{total}=1.6*10^6 and \eta=0.04 can generate data for Figure S26A, S26B and 5D.
   We name this file: deltaT_eta_0_04.dat.

The code 'compute_rate_constants.py' can be used to compute the upper polariton to dark state decay
rate. It produces files 'rate_const_0_02.txt', 'rate_const_0_04.txt', 'rate_const_0_08.txt' when
eta equals 0.02, 0.04, 0.08, respectively (change values for variables 'filename' and 'eta' in code).

The code 'plot_rate_constants_and_dT.py' produces Figures 5D, S25A, S25B, S26A and part of S26B taking 
the following files as inputs:

1) rate_const_0_02.txt
2) rate_const_0_04.txt
3) rate_const_0_08.txt
4) deltaT_eta_0_02.dat
5) deltaT_eta_0_04.dat
6) deltaT_eta_0_08.dat
7) deltaT_R_5.dat
8) deltaT_R_6.dat
9) deltaT_R_7.dat
10) deltaT_R_8.dat

#####################################################################################################
