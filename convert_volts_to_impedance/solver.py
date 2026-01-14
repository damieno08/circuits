#!/usr/bin/env python

# Imports
#
import numpy as np
import sys

# Function will take in voltage ratio and desired
# unit then print conversion
#
def convert_to_impedance(ratio, unit):
        
        R1 = 100 # ohms from resistor in series

        # Convert to impedance
        #
        ohms = R1 * 10 ** (ratio/20) # ohms

        # Check if we want ohms or dB
        #
        if unit == "db":
                return 20*np.log10(ohms) 
        return ohms
                
# Driver program
#
def main(argv):

        # Create list of valid units
        #
        s = {"ohms", "ohm", "db"}

        # Try to get inputs and throw errors if we fail
        #
        try: 
                inputVoltRatio = float(argv[1]) # dB
                desiredUnit = argv[2].lower() # Either ohms or dB
                
        except:
                print("Error with inputs")
                print("Usage: solver.py [voltage ratio in volts] [desired unit: dB/ohms]")
                sys.exit(1)

        # Check if units are on list
        #
        if desiredUnit not in s:
                print("Please only enter valid desired units")
                print("Usage: solver.py [voltage ratio in volts] [desired unit: dB/ohms]")
                sys.exit(1)

        # Create and print answer if on list
        #
        Z = convert_to_impedance(inputVoltRatio, desiredUnit)
        print("The conversion is %.3f [%s]" % (Z, desiredUnit))

        
	# Exit gracefully
        #
        return True

# Begin gracefully
#
if __name__ == '__main__':
	main(sys.argv[0:])
        
# End of file
