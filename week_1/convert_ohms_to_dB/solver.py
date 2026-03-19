#!/usr/bin/env python

# Program will take in starting value and unit
# then output the conversion
#

# imports
#
import sys
import numpy as np

# Function takes in base value and unit
# then returns the converted value and unit
#
def convert(value, unit):

        # Initialize to trivial value
        #
        conversion = 0

        # Check which conversion to perform
        #
        if unit == "ohms":
                conversion = 20*np.log10(value)
                unit = "dB"
        else:
                conversion = 10 ** (value/20)
                unit = "ohms"

        # return value and unit
        #
        return conversion, unit

# Driver program
#
def main(argv):

        # Take inputs and throw errors
        #
        try:
                inputNum = float(argv[1])
                inputUnit = argv[2]
                inputUnit = inputUnit.lower()

        except:
                print("Error with inputs")
                print("Usage: solver.py [value] [ohms/dB]")
                sys.exit(1)


        # Check for proper units
        #
        if inputUnit == "ohms" or inputUnit == "ohm":
                inputUnit = "ohms"
        elif inputUnit == "db":
                inputUnit = "db"
        else:
                print("Incorrect units provided")
                print("Usage: solver.py [value] [ohms/dB]")
                sys.exit(1)

        # Convert to other unit and print
        #
        outputNum, unit = convert(inputNum, inputUnit)
        print("The conversion is: %.3f %s" % (outputNum , unit)) 
                
	# Exit gracefully
        #
        return True

# Begin gracefully
#
if __name__ == '__main__':
	main(sys.argv[0:])
        
# End of file
