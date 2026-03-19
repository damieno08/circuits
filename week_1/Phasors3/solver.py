#!/usr/bin/env python

# Program will take in 

# Imports
#
import numpy as np
import sys

# Functions
#

# takes in complex number and returns its angle [deg] and magnitude
#
def mag_angle(complex_num):
    mag = abs(complex_num) # same unit as original
    angle = np.degrees(np.arctan(complex_num.imag/complex_num.real)); # degrees
    return mag, angle

# Driver Program
#
def main(argv):

        # Will error check inputs and print exit message
        # on failure
        #
        try:
                R = float(argv[1]) # ohms
                C = float(argv[2]) * 10 ** -6 # farads
                L = float(argv[3]) * 10 ** -3 # henries
                w = 2 * np.pi * 100 # angular frequency
                f = w / (2*np.pi) # hz
                V_S = 1 # volts
                
        except:
                print("Error with inputs")
                print("Usage: solver.py [R in ohms] [C in microfarads] [L in millihenries]")
                sys.exit(1)

        # Calculate impedance for each component then
        # for entire circuit
        #
        Z_C = -1j/(w*C) # ohms
        Z_L = 1j*w*L # ohms
        Z_R = R

        Z_ab = Z_C + Z_L + Z_R # ohms

        # Calculate overall current based on impedance
        #
        I = V_S/ Z_ab # amps
        I_mag, I_ang = mag_angle(I) # amps, degrees


        # Calculate the voltage on capacitor based on
        # calculated current
        #
        VC = Z_C*I # volts
        VC_mag, VC_ang = mag_angle(VC) # volts, degrees

        # Print our final results
        #
        print("The real portion of impedance is %.3f [ohms]" % Z_ab.real)
        print("The imaginary portion of impedance is %.3f [ohms]" % Z_ab.imag)
        print("The magintude of the voltage VC is %.3f [V]" % VC_mag)
        print("The angle of the voltage VC is %.3f [deg]" % VC_ang)
        print("The magintude of the current I is %.3f [mA]" % (I_mag*1000))
        print("The angle of the current I is %.3f [deg]" % I_ang)
        print("The angular frequency of our circuit is %.3f [rads/sec]" % w)
        print("The frequency of our circuit is %.3f [hz]" % f)
        
	# Exit gracefully
        #
        return True

# Begin gracefully
#
if __name__ == '__main__':
	main(sys.argv[0:])
        
# End of file
