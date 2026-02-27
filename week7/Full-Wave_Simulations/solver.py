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

        except:
                print("Usage: solver.py [Source voltage in volts] [Resistance in kohms]")
                sys.exit(1)

        # set forward voltages
        V_F1 = 0.7 # V
        V_LED = 1.79 # V
                
        # voltage drop across resistor
        V_OUT1 = V_IN - 2 * V_F1 # V
        V_OUT2 = V_IN - 2 * V_LED # V

        # current across loop
        I1 = (V_OUT1/R) * 1000 # mA
        I2 = (V_OUT2/R) * 1000 # mA
        
        # print results
        print("\nThe output voltage with a diode is %.3f[V]" % V_OUT1)
        print("The current with a diode is %.3f[mA]" % I1)
                
        print("\nThe output voltage with the yellow LED is %.3f[V]" % V_OUT2)
        print("The current with a yellow LED is %.3f[mA]\n" % I2)
        
        # exit gracefully
        return True

# begin gracefully
if __name__ == '__main__':
	main(sys.argv[0:])
# End of file
