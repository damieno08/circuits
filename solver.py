#!/usr/bin/env python

# This program will take RLC circuit
# with R1 and C in series with parallel
# combination of R2 L and find voltage 
# across R1 and C (V1), voltage across
# R2 and L (V2), overall current (I), 
# Current across L (I1), and current across
# R2 (I2). We find magnitudes and angles
# using Phasors for analysis

# imports
#
import numpy as np
import sys
import os

# functions
#

# takes in complex number and returns its angle [deg] and magnitude
#
def mag_angle(complex_num):
    mag = abs(complex_num) # same unit as original
    angle = np.degrees(np.arctan(complex_num.imag/complex_num.real)); # degrees
    return mag, angle

# will check if values are within tolerance for voltage/current drops
#
def check_tol(original, drops, tolerance):

    # Check if we are in percent tolerance for either
    # voltage or current drops
    #
    er = (original-sum(drops))/original*100
    if er < tolerance:
        return True

    # Tell user they fail tolerance
    #
    return False

# driver function
#
def main(argv):

    # check that all values are made
    #
    if len(argv) != 5:
        print("Error: Incorrect number of arguments")
        print("Usage: [R1 in Kohms] [R2 in Kohms] [C in nanofarads] [L in milihenry]")
        sys.exit(1)

    try:
        
        # Input values for RLC
        #
        R1 = float(argv[1]) * 1000; # ohms
        R2 = float(argv[2]) * 1000; # ohms
        C = float(argv[3]) * 10 ** -9; # farads
        L = float(argv[4])*10 ** -3; # henries
        phi = 0; # degrees
        w = 10**6; # angular frequency

    except:
        print("Errors with input values")
        print("Usage: [R1 in ohms] [R2 in ohms] [C in nanofarads] [L in milihenry]")
        sys.exit(1)
        
    V_S = 16*np.exp(1j*phi); # Volts
    
    # Perform calculation for R1 and C impedance
    #
    Z_R1 = R1; # ohms
    Z_C = -1j/(w*C); # ohms
    Z_S = Z_R1 + Z_C; # ohms
    
    # Perform calculation for impedance across parallel
    # combination
    #
    Z_L = 1j*w*L; # ohms
    Z_R2 = R2; # ohms
    Z_P = (Z_L*Z_R2)/(Z_L+Z_R2); # ohms
    
    # Calculate total impedance by combining the two
    #
    Z_ab = Z_S + Z_P; # ohms
    
    # Calculate overall current I
    #
    I = V_S/Z_ab; # amp
    I_mag, I_ang = mag_angle(I) # amps, degrees
    
    # Calculate magnitude and angle for voltages
    #
    V1 = I*Z_S; # volts
    V1_mag, V1_ang = mag_angle(V1) # volts, degrees
    
    V2 = I*Z_P; # volts
    V2_mag, V2_ang = mag_angle(V2) # volts, degrees
    
    # Calculate magnitued and angle for currents
    #
    I1 = V2/Z_L # amps
    I1_mag, I1_ang = mag_angle(I1) # amps, degrees
    
    I2 = V2/Z_R2 # amps
    I2_mag, I2_ang = mag_angle(I2) # amps, degrees
    
    if check_tol(V_S,[V1, V2], 5) and check_tol(I, [I1, I2], 5):
        # Print final results after sanity check
        #
        print("The real portion of overall impedance is %.3f [KOhms]\n" % (Z_ab.real/1000))
        print("The imaginary portion of overall impedance is %.3f [KOhms]\n" % (Z_ab.imag/1000))
        print("The magnitude of the current I is %.3f [mA]\n" %  (I_mag*1000))
        print("The angle of the current I is %.3f [deg]\n" %  I_ang)
        
        print("The magnitude of the voltage V1 is %.3f [V]\n" % V1_mag)
        print("The angle of the voltage V1 is %.3f [deg]\n" %  V1_ang)
        
        print("The magnitude of the voltage V2 is %.3f [V]\n" % V2_mag)
        print("The angle of the voltage V2 is %.3f [deg]\n" %  V2_ang)
        
        print("The magnitude of the current I1 is %.3f [mA]\n" % (I1_mag*1000))
        print("The angle of the current I1 is %.3f [deg]\n" %  I1_ang)
        
        print("The magnitude of the current I2 is %.3f [mA]\n" % (I2_mag*1000))
        print("The angle of the current I2 is %.3f [deg]\n" %  I2_ang)

        print("The frequency of all time domain signals is %.3f [kHz]" % (w/(2*np.pi*1000)))
    else:
        print("Too many significant errors in calculation")
        

# Begin gracefully
#
if __name__ == '__main__':
    main(sys.argv[0:])

# End of file
