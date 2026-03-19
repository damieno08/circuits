#!/usr/bin/env python

# file: /home/tut62308/circuits/week10/NMOS/solver/solver.py
#
# Version History: 
# 20260318 create initial file

# This program will solve the P-Channel MOSFET prequiz for circuits 2.
# This is a P-channel mosfet in series with a resistor given a desired
# current across the total circuit.


# imports
import sys

# will take in the source-drain voltage and threshold to find region
# of operation for NMOS
def find_region(V_SG, V_TH):

        # placehold output
        region = ""       

        # check if we are above cutoff
        if (V_SG < V_TH):
                region = "OFF"
        else:
                region = "ON"

        # return the answer
        return region

# function will determine the current provided by the MOSFET
def find_current(V_S, R):

        # calculate and return current in amps
        return  V_S/R

# driver function
def main(argv):

        
        # try to get input variables
        try:
                V_GS = float(argv[1])
                V_TH = abs(float(argv[2]))
                R = float(argv[3])
                V_S = float(argv[4])
        except:
                # throw error if missing something
                print("Error with usage.")
                print("Usage: [gate-source voltage in volts] [threshold voltage in volts] [R in ohms] [source voltage in volts]")
                exit(1)

        V_SG = -V_GS # volts
        
        region = find_region(V_SG, V_TH)

        I = 0
        
        if(region=="ON"):
                I = find_current(V_S, R) # amps
                

        print(f"The MOSFET is {region}. The current produced is {I * 1000: .3f}[mA]")
        
        # exit gracefully
        return True

# begin gracefully
if __name__ == '__main__':
	main(sys.argv[0:])
        
# End of file
