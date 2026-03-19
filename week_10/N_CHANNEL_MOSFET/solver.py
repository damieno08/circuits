#!/usr/bin/env python

# file: /home/tut62308/circuits/week10/N_CHANNEL_MOSFET/solver.py

# Version History: 
# 20260318 create initial file

# Program will find the current through an N channel mosfet connected to resistor.

# Imports
import sys

# driver function
def main(argv):

        # try to extract variables
        try:
          V_DD = float(argv[1]) # volts
          V_GS = float(argv[2]) # volts
          V_TH = float(argv[3]) # volts
          R = float(argv[4]) # ohms
          
        except:
                # tell user error and exit
                print("Error: incorrect usage")
                print("Usage: solver.py [V_DD in volts] [V_GS in volts] [V_TH in volts] [R in ohms]")
                exit(1)

        # find "on" voltage
        V_OV = V_GS - V_TH # volts

        # placehold current value
        I_D = 0 # amps

        # check region
        if (V_GS <= V_OV):
                print("MOSFET is in cutoff region.")
        else:
                print("MOSFET is in satured region.")
                I_D = V_DD/R # amps
        print(f"The current is {I_D * 1000: .2f}[mA].")
                
        # exit gracefully
        return True

# begin gracefully
if __name__ == '__main__':
	main(sys.argv[0:])
# End of file
