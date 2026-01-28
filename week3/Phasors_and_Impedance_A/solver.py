#!/usr/bin/env python

# file: /home/tut62308/circuits/week3/Phasors_and_Impedance_A/solver/solver.py
#

# Program will solve an RLC circuit where C is in series with the
# RL combination at set frequency

# Version History: 
# 20260128 create initial file

# Imports
import sys
import numpy as np
import math

# Functions

def mag_angle(complex_num):
    mag = abs(complex_num) # same unit as original
    angle = np.degrees(np.arctan2(complex_num.imag, complex_num.real)); # degrees
    return mag, angle

# Driver
def main(argv):

    # Check if user provided terminal inputs
    #
    try:
        V_S = 1 # Volts amplitude
        C = int(argv[3]) * 10 ** -9 # nanofarads
        R2 = int(argv[1]) * 1000 # kilohms
        L = int(argv[2]) * 10 ** -3 # milihenries

    except:
        print("Using default values as input failed")
        C = 1 * 10 ** -9 # farad
        R2 = 4000 # ohms
        L = 3 * 10 ** -3 # henry
        
    f = 100 * 10 ** 3 # Hz
    w = 2 * np.pi * f # radians
    
    Z_L = 1j * w * L # Ohms
    Z_C = 1/( 1j * w * C) # Ohms
    Z_R2 = R2 # Ohms

    Z_R2L = Z_R2*Z_L / (Z_R2+Z_L) # RL combination

    # total impedance
    Z_ab = Z_R2L + Z_C # Ohms
    Z_RE = Z_ab.real # real impedance        
    Z_IM = Z_ab.imag # imaginary impedance
    
    I_T = V_S/Z_ab # Total current in amps
    # Get magnitude and angle of current
    [It_mag, It_ang] = mag_angle(I_T) # amps, degrees

    V_C = I_T * Z_C # Volts

    V_T = V_S - V_C # Volts

    # Get magnitude and angle of voltage
    [Vt_mag, Vt_ang] = mag_angle(V_T)
    
    I_L = V_T / Z_L # Amps
    [IL_mag, IL_ang] = mag_angle(I_L) # amps, degrees

    # Convert all to RMS

    VS_RMS = V_S * 2 ** (-1/2) # Volts rms
    VT_RMS = Vt_mag * 2 ** (-1/2) # Volts rms
    IL_RMS = IL_mag * 2 ** (-1/2) # Amps rms
    IT_RMS = It_mag * 2 ** (-1/2) # Amps rms

    P_consumed = VS_RMS ** 2 / abs(Z_ab) # Watts

    P_supplied = -P_consumed # Watts
    
    # Print all results
    print("The real impedance is %.3f[ohms]." % Z_RE)
    print("The imaginary impedance is %.3f[ohms]." % Z_IM)
    print("The magnitude of the current i(t) is %.3f [mA]" %  (It_mag*1000))
    print("The angle of the current i(t) is %.3f [deg]" %  It_ang)
    print("The magnitude of the current i_L(t) is %.3f [mA]" %  (IL_mag*1000))
    print("The angle of the current i_L(t) is %.3f [deg]" %  IL_ang)
    print("The magnitude of the voltage v(t) is %.3f [V]" %  Vt_mag)
    print("The angle of the voltage v(t) is %.3f [deg]" %  Vt_ang)
    print("The rms voltage of the source is %.3f[V]" % VS_RMS)
    print("The rms voltage of v(t) is %.3f[V]" % VT_RMS)
    print("The rms current of i_L(t) is %.3f[mA]" % (IL_RMS * 1000))
    print("The rms current of i(t) is %.3f[mA]" % (IT_RMS * 1000))
    print("The average power consumed is %.3f[mW]" % (P_consumed*1000))
    print("The average power supplied is %.3f[mW]" % (P_supplied*1000))
    
    # exit gracefully
    return True

# begin gracefully
if __name__ == '__main__':
	main(sys.argv[0:])
# End of file
