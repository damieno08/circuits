#!/usr/bin/env python

# file: /home/tut62308/circuits/week7/solver/solver.py

# This program will solve week 7 preclass quiz involving multiple series diodes

# Version History: 
# 20260227 create initial file

# imports
import os
import sys
import numpy as np
import math

# main function
def main(argv):

        # set forward voltage of all diodes 
        V_F = 0.7 # V
        num_diodes = 3 # number of diodes in simulation

        # Try to get values from user
        try:
                V_S = float(argv[1]) # Source Voltage in volts
                R_1 = float(argv[2]) * 1000 # Ohms
                R_2 = float(argv[3]) * 1000 # Ohms
                R_3 = float(argv[4]) * 1000 # Ohms
                
        except:
                # Tell user about proper usage and exit with error
                print("Usage: solver.py [Source Voltage] [Resistor 1 in kohms] [Resistor 2 in kohms]  [Resistor 3 in kohms]")
                sys.exit(1)

        R_EQ = R_1 + R_2 + R_3 # series resistance equivalent
                
        # Calculate voltage across series resistor combination
        V_R123 = V_S - V_F*(num_diodes) # Volts

        # Calculate the current across loop
        I = V_R123 / R_EQ # Amps

        # Calulate all voltages of resistors
        V_R1 = I * R_1 # Voltage
        V_R2 = I * R_2 # Voltage
        V_R3 = I * R_3 # Voltage
                
        # Calculate power of diodes and resistors
        P_R1 = R_1 * (I ** 2)*1000 # mW
        P_R2 = R_2 * (I ** 2)*1000 # mW
        P_R3 = R_3 * (I ** 2)*1000 # mW
        P_D1 = V_F * I*1000 # mW
        P_D2 = V_F * I*1000 # mW
        P_D3 = V_F * I*1000 # mW
                
        # print results

        print("\nThe current across the loop is %.3f[mA]" % (I*1000))
        
        print("\nThe voltage across R1 is %.3f[V]." % V_R1)
        print("The power dissipated by R1 is %.3f[mW]." % P_R1)
        
        print("\nThe voltage across R2 is %.3f[V]." % V_R2)
        print("The power dissipated by R2 is %.3f[mW]." % P_R2)
        
        print("\nThe voltage across R3 is %.3f[V]." % V_R3)
        print("The power dissipated by R3 is %.3f[mW]." % P_R3)
        
        print("\nThe power dissipated by D1 is %.3f[mW]." % P_D1)
        print("\nThe power dissipated by D2 is %.3f[mW]." % P_D2)
        print("\nThe power dissipated by D3 is %.3f[mW].\n" % P_D3)
        
        # exit gracefully
        return True

# begin gracefully
if __name__ == '__main__':
	main(sys.argv[0:])
        
# end of file
