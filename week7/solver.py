#!/usr/bin/env python

# file: /home/tut62308/circuits/week7/solver/solver.py

# This program will solve week 7 preclass quiz involving two parallel paths containing
# a resistor and diodes. Only the loop with diode 2 and resistor 2 will conduct

# Version History: 
# 20260227 create initial file

# imports
import os
import sys
import numpy as np
import math

# main function
def main(argv):

        # set forward voltage of both diodes 
        V_F = 0.7 # V

        # Try to get values from user
        try:
                V_S = float(argv[1]) # Source Voltage in volts
                R_2 = float(argv[3]) # Resistance across actually conducting path

        except:
                # Tell user about proper usage and exit with error
                print("Usage: solver.py [Source Voltage] [Resistor 1 in ohms] [Resistor 2 in ohms]")
                sys.exit(1)

        # Calculate voltage across resistor 2
        V_R2 = V_S - V_F # Volts

        # Calculate the current across loop that conducts
        I_2 = V_R2 / R_2 # Amps

        # Calculate power of diode and resistor
        P_D2 = I_2 * V_F # Watts
        P_R2 = I_2 * V_R2 # Watts


        # print results
        print("\nThe voltage across R1 is 0[V].")
        print("The power dissipated by R1 is 0[W].")
        
        print("\nThe voltage across R2 is %.2f[V]." % V_R2)
        print("The power dissipated by R2 is %.3f[W]." % P_R2)

        print("\nThe power dissipated by D2 is %.3f[W]." % P_D2)
        print("\nThe power dissipated by D1 is 0[W].\n")
        
        
        # exit gracefully
        return True

# begin gracefully
if __name__ == '__main__':
	main(sys.argv[0:])
        
# end of file
