#!/usr/bin/env python

# file: /home/tut62308/circuits/week5/solver/solver.py
#
# Version History: 
# 20260209 create initial file

# imports
import os
import sys
import numpy as np
import math

# takes in complex number and returns its angle [deg] and magnitude
#
def mag_angle(complex_num):
    mag = abs(complex_num) # same unit as original
    angle = np.degrees(np.arctan(complex_num.imag/complex_num.real)); # degrees
    return mag, angle

# solve frequency magnitude for a transfer function
#
def transfer(R,C,w, kind):

    if kind == "C":
        H = (1/(R*C)) / (1j*w + 1/(R*C))
    elif kind == "R":
        H = 1j*w/(1j*w + 1/(R*C))
    H_mag, H_ang = mag_angle(H)
    return H_mag, H_ang

# convert ratio to dB
#
def convert_to_db(num):
        return 20*math.log(num,10) # dB
   
# main function
#
def main(argv):

    # space answer from command line
    #
    print()

    # test inputs for proper types
    #
    try:
        R = float(argv[1]) * 10 ** 3 # ohms
        C = float(argv[2]) * 10 ** -6 # farads
        f = float(argv[3]) # hz

    # tell user about mistake with usage
    #
    except:
        print("Error with user input")
        print("Usage: solver.py [Resistor in kohms] [Capacitor in microfarads] [Frequency in hz]")
        sys.exit(1)

    # convert to angular frequency
    #
    w = 2*np.pi*f

    # calculate magnitude and angle of transfer function
    # for low pass
    #
    H_mag, H_ang = transfer(R,C,w,"C")
    H_DB = convert_to_db(H_mag)

    # print values for low pass measurements
    #
    print("Values for low pass (Vc/Vs)")
    print("Magnitude: %.3f[dB]" % H_DB)
    print("Angle: %.3f[degrees]" % H_mag)

    # calculate magnitude and angle of transfer function
    # for high pass
    #
    H_mag, H_ang = transfer(R,C,w,"R")
    
    H_DB = convert_to_db(H_mag)
    print("\n")
    print("Values for high pass")
    print("Magnitude: %.3f[dB]" % H_DB)
    print("Angle: %.3f[degrees]" % H_mag)
    print("\n")
    
    # find and print cutoff frequency
    #
    cutoff_freq = 1/(2*np.pi*R*C)
    print("Cutoff is %.3f[Hz]" % cutoff_freq)

    # space out from command line
    #
    print("")
    
    # exit gracefully        
    return True

# begin gracefully
if __name__ == '__main__':
	main(sys.argv[0:])
# End of file
