# -*- coding: utf-8 -*-
"""
Created on Thu Nov 17 21:30:46 2015

SAR Single Channel ADC PWL (Piece Wise Linear) Script. This script writes to
text files. The text file contains two columns: time on the first column and
voltage on the second column. The text files would then be sent to the PWL
signal generator on LTSPICE for fast and slow signal PWL generators.

Usage:
 0. save this file to your desktop
 1. open cmd 
 2. type: cd C:\Users\funsten1\Desktop
 3. type: python brads_script.py > timing.txt
 4. type: notepad timing.txt
 
@author: Brad Funsten and Matthew Dayton
Lawrence Livermore National Laboratory
Versions: V2.0
"""

import numpy as np # for array arithmetic
import pandas as pd # easy ploting

filename1 = 'PWL.txt' # Fast and slow slew rate voltage PWL and time
filename2 = 'SW.txt' # Switch voltage and time
filename3 = 'VTGT.txt' # ideal integrator voltage and time

VREF = 1.65 # reference voltage
Rfast = 2.56e3 # fast resistor
Rslow = 655.36e3 # slow resistor
C = 1e-9 # integrator capacitor
Tclk = 10e-9 # fpga clock
Texp = int(-np.log(Tclk)/np.log(10))# exponent global, used for rounding later

# Parameters
SR_fast = VREF / (Rfast * C) # fast slew rate
SR_slow = VREF / (Rslow * C) # slow slew rate
V_CH = 1 # analog voltage channel 43690
n_bit_fast = 8 # number of bits for fast PWL
n_bit_slow = 8 # number of bits for slow PWL

#compute times
tf = (Rfast * C)
ts = (Rslow * C)

#checks two voltages and returns the vout and sign results
def vcheck(V1,V2):
    if V1 > V2:
        Vout = 3.3
        sign = 1
    else:
        Vout = 0.0
        sign = -1
    return Vout,sign
    
# the render PWL functions by print out the steps to stdout
def render(Vtgt,V_CH,V0,dV,time,dT,n,filename,fast): 
    for i in range(1,n+1):
        Vout,sign = vcheck(V_CH,Vtgt)
        if not(i==1 and fast==True):
            time = time + dT
            if(i==8 and fast==True): time+=Tclk/2
            print time-Tclk/2,3.3 - V0,dT,Vtgt        
            outFile1.write('{:.8e} {:4.2f}\n'.format(time-Tclk/2,3.3 - V0)) # write before transition
            points.append([time-Tclk/2,3.3 - V0])
            if(i==8 and fast==True): time-=Tclk/2
        
        outFile3.write('{:.8e} {:4.10f}\n'.format(time,Vtgt)) # write before transition

        if(i==8 and fast==True): time+=Tclk/2
        print time+Tclk/2,3.3 - Vout,dT,Vtgt,dV
        outFile1.write('{:.8e} {:4.2f}\n'.format(time+Tclk/2,3.3 - Vout)) # write after transition
        ## store some test stuff for ploting,comment out if not needed
        points.append([time+Tclk/2,3.3 - Vout]) 
        if(i==8 and fast==True): time-=Tclk/2
        
        V0 = Vout        
        dT = round(dT/2,Texp) # assume FPGA clock forces us to round
        dV = dV/2
        Vtgt = Vtgt + sign*dV
    return Vtgt,Vout,V0,dV,time


# now that the functions are defined,
#initialize some variables and begin
Vtgt = VREF
#Vtgt_d = 0.0 # delayed version of Vtarget
V0   = 3.3  # last output to integrator
time = 0.0
#sign = -1

points = []

outFile1=open(filename1,'w') # Open filename text  
outFile2=open(filename2,'w') # Open filename text 
outFile3=open(filename3,'w') # Open filename text 
#print 0,1.65        
#outFile1.write('{:.8e} {:4.2f}\n'.format(0,1.65)) # write before transition
#points.append([0,1.65])
outFile2.write('{:.8e} {:3.1f}\n'.format(0,3.3)) # write before transition

#spit out the fast signals first, added a bit to account for the first conversion
#print '## fast signal'
#print time,VREF
#outFile1.write('{:.8e} {:4.2f}\n'.format(time,VREF)) # write before transition
#time += 0.1e-6
Vtgt,Vout,V0,dV,time= render(Vtgt,V_CH,V0,VREF,time,tf,n_bit_fast,filename1,fast=True)
outFile2.write('{:.8e} {:3.1f}\n'.format(time-Tclk/2,3.3)) # write before transition
outFile2.write('{:.8e} {:3.1f}\n'.format(time+Tclk/2,0)) # write after transition
#spit out the slow signal. 
#print '## slow signal'
Vtgt,Vout,V0,dV,time =render(Vtgt,V_CH,Vout,dV,time,(dV*ts/VREF),n_bit_slow,filename1,fast=False)
outFile2.write('{:.8e} {:3.1f}\n'.format(time,0)) # write after transition
outFile1.close() # close file 
outFile2.close() # close file 
outFile3.close()
                            
#### solution check
#print '## check answer'
#print 'A:', bin(np.uint16((int(V_CH*65535/3.3))))
#print 'Result:', np.array(np.array(test,dtype=bool).astype('int')), 'Bits =',len(test)
#print 'V_CH =', Vtgt,' = ',(V_CH-Vtgt)

## plot points here
df = pd.DataFrame(points)
df.set_index(0,inplace=True)
df.plot()

# EOF