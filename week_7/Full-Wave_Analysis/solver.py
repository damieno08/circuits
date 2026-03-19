#!/usr/bin/env python

# file: /home/tut62308/circuits/week7/Half-Wave_Analysis/solver/solver.py

# Program will solve the full-wave rectifier simulation model.

# Version History: 
# 20260227 create initial file

# imports
import os
import sys
import numpy as np
import math

# main function
def main(argv):

        try:
                V_IN = float(argv[1]) # source voltage
                R = float(argv[2]) * 1000 # ohms
                V_F = float(argv[3]) # forward voltage

        except:
                print("Usage: solver.py [Source voltage in volts] [Resistance in kohms] [Diode forward voltage in volts]")
                sys.exit(1)

        # voltage drop across resistor
        V_OUT = V_IN - 2 * V_F # V

        # current across loop
        I = (V_OUT/R) * 1000 # mA

        # print results
        print("\nThe output voltage is %.3f[V]" % V_OUT)
        print("\nThe current is %.3f[mA]\n" % I)
        
        # exit gracefully
        return True

# begin gracefully
if __name__ == '__main__':
	main(sys.argv[0:])
# End of file
