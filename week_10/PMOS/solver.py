#!/usr/bin/env python

# file: /home/tut62308/circuits/week10/NMOS/solver/solver.py
#
# Version History: 
# 20260318 create initial file

# This program will solve the PMOS prequiz for circuits 2. This is a PMOS
# transistor in series with a resistor given a desired current
# across the total circuit.


# imports
import sys

# will take in the source-drain voltage and threshold to find region
# of operation for NMOS
def find_region(V_SG, V_SD, V_TH):
        
        region = ""
        
        # find on voltage
        V_OV = V_SG-V_TH

        # check if we are above cutoff
        if (V_SG < V_TH):
                region = "Cutoff"
                
        # determine region
        if(abs(V_OV) > V_SG):
                region = "Triode"
        else:
                region = "Saturation"

        # return the answer
        return region, V_OV

# function will determine the width of the transistor after being given
def find_width_and_resistance(i_D=0.0001, L=1, k=1, V_OV=1, region="Saturation", V_SD=1):

        R = (1.8 - V_SD)/ i_D
        
        # calculate width based on region and values
        if (region == "Saturation"):
                # return calculated width
                return R, (2 * i_D * L)/(k * V_OV ** 2)
        elif (region == "Triode"):
                return R, (i_D * L) / (k * (V_OV - V_SD * 0.5) * V_SD)
        else:
                print("Error: region must be triode or saturation to solve for width.")
                exit(1)

# driver function
def main(argv):

        # place constants
        V_DD = 1.8 # volts
        
        # try to get input variables
        try:
                V_TH = abs(float(argv[1])) # volts
                k = float(argv[2]) * 10 ** -6 # A/V^2
                L = float(argv[3]) * 10 ** -6 # m
                I_D = float(argv[4]) * 10 ** -6 # A
                V_D = float(argv[5]) # volts
        except:
                # throw error if missing something
                print("Error with usage.")
                print("Usage: [Threshold voltage] [process trandsconductance parameter] [length in micrometers] [I_D in microamps] [V_D in volts]")
                exit(1)

        V_SG = V_DD - V_D # volts
        V_SD = V_SG # volts
        
        region, V_OV = find_region(V_SG, V_SD, V_TH)

        R, width = find_width_and_resistance(I_D, L, k, V_OV,region, V_SD)

        print(f"The width is {width * 10 ** 6: .4f}[um]. The resistance value is {R / 1000: .4f}[kohm]")
        
        # exit gracefully
        return True

# begin gracefully
if __name__ == '__main__':
	main(sys.argv[0:])
        
# End of file
