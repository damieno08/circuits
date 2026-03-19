#!/usr/bin/env python

# This program will take RLC circuit
# with C in series with the parallel combination of
# L and R2 and outputs the impedance

# imports
#
import numpy as np
import sys
import os

# functions
#

# driver function
#
def main(argv):   

    # Input values
    #
    phi = 0
    V_S = 16*np.exp(1j*phi); # Volts
    C = 10**-9 # farads
    R2 = 4 * 10 ** 3 # ohms
    L = 3 * 10 ** -3 # henries
    w = 2*np.pi * 100 * 10 ** 3 # angular frequency
    
    # Calculate impedance of capacitor and parallel
    # combination
    #
    Z_C = -1j/(w*C) # ohms
    
    Z_R2 = R2 # ohms
    Z_L = 1j*w*L # ohms

    Z_P = (Z_R2 * Z_L)/(Z_R2 + Z_L) # ohms

    # Give final impedance
    #
    Z_ab = Z_C + Z_P # ohms

    # Print our result
    #
    print("The real portion of impedance is %.3f [ohms]" % Z_ab.real)
    print("The imaginary portion of impedance is %.3f [ohms]" % Z_ab.imag)

    # Exit gracefully
    #
    return True
    
# Begin gracefully
#
if __name__ == '__main__':
    main(sys.argv[0:])

# End of file
