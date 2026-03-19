#!/usr/bin/env python

# file: /home/tut62308/circuits/week3/Phasors_and_Impedance_B/solver/solver.py
#
# Version History: 
# 20260128 create initial file

# Program will calculate values for an RLC circuit with all components in
# series and set frequency

# Imports

import sys
import os
import numpy as np

# Functions

# Will find magnitude and angle of complex number
def mag_angle(complex_num):
    mag = abs(complex_num) # same unit as original
    angle = np.degrees(np.arctan2(complex_num.imag, complex_num.real)); # degrees
    return mag, angle

def main(argv):
        try:
                V_m = float(argv[1]) # volts
                R = float(argv[2]) # ohms
                C = float(argv[3]) * 10 ** -6 # farads
                L = float(argv[4]) * 10 ** -3 # henries
        except:
                print("Please provide proper inputs")
                print("Usage: solver.py [V_m in volts] [R in ohms] [C in microfarad] [L in milihenry] ")
                sys.exit(1)
                
        f = 100 # Hz
        w = 2 * np.pi * f # radians
                
        Z_C = 1/(1j*w*C)
        Z_L = 1j*w*L
        Z_R = R

        Z_ab = Z_C + Z_L + Z_R # ohms        

        I_T = V_m / Z_ab # amps
        [It_mag, It_ang] = mag_angle(I_T) # amps, degrees

        VS_RMS = V_m * 2 ** (-1/2)

        I_RMS = It_mag * 2 ** (-1/2) # amps

        P_Used = (I_RMS ** 2) * R # Watts
        P_Source = -P_Used # Watts

        # Print all results
        print("The rms voltage of the source is %.3f[V]" % VS_RMS)
        print("The real impedance is %.3f[ohms]." % Z_ab.real)
        print("The imaginary impedance is %.3f[ohms]." % Z_ab.imag)
        print("The magnitude of the current i(t) is %.3f [mA]" %  (It_mag*1000))
        print("The rms current of i(t) is %.3f[mA]" % (I_RMS * 1000))
        print("The average power consumed is %.3f[mW]" % (P_Used*1000))
        print("The average power supplied is %.3f[mW]" % (P_Source*1000))        
        
	# exit gracefully
        return True
# begin gracefully
if __name__ == '__main__':
	main(sys.argv[0:])
# End of file
