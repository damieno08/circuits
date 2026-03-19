#!/usr/bin/env python

# file: /home/tut62308/circuits/week10/NMOS/solver/solver.py
#
# Version History: 
# 20260318 create initial file

# This program will solve the NMOS prequiz for circuits 2. This is two NMOS
# transistors in series with a desired current across the total circuit.
# These transistors are connected source to drain.

# imports
import sys

# will take in the drain-source voltage and threshold to find region
# of operation for NMOS
def find_region(V_GS, V_DS, V_TH):
        
        region = ""
        
        # find on voltage
        V_OV = V_GS-V_TH

        # check if we are above cutoff
        if (V_GS < V_TH):
                region = "Cutoff"
                
        # determine region
        if(V_OV > V_DS):
                region = "Triode"
        else:
                region = "Saturation"

        # return the answer
        return region, V_OV

# function will determine the width of the transistor after being given
def find_width(i_D=0.0001, L=1, k=1, V_OV=1, region="Saturation", V_DS=1):

        # calculate width based on region and values
        if (region == "Saturation"):
                # return calculated width
                return (2 * i_D * L)/(k * V_OV ** 2)
        elif (region == "Triode"):
                return (i_D * L) / (k * (V_OV - V_DS * 0.5) * V_DS)
        else:
                print("Error: region must be triode or saturation to solve for width.")
                exit(1)

# driver function
def main(argv):

        # place constants
        V_S = 1.8 # volts
        I_D = 0.0001 # amps

        # check if they want resistance instead
        if(len(argv) == 2):
                try:
                        V_DS = float(argv[1])
                except:
                        print("Error: V_DS must be a number")
                        exit(1)
                R = (V_S - V_DS)/I_D # ohms
                R/=1000 # kohms
                print("The resistance is %.2f[kohms]" % R)
                exit(0)
        
        # try to get input variables
        try:
                V_TH = float(argv[1]) # volts
                k = float(argv[2]) * 10 ** -6 # A/V^2
                L = float(argv[3]) * 10 ** -6 # m
        except:
                # throw error if missing something
                print("Error with usage.")
                print("Usage: solver.py [Threshold voltage] [process trandsconductance parameter] [length in micrometers]")
                print("Alternate usage: solver.py [DS voltage]")
                exit(1)

        # find all voltages, regions, and widths
        V_DS1 = 0.8 # volts
        V_GS1 = V_DS1 # volts

        region_1, V_OV_1 = find_region(V_DS1, V_GS1, V_TH)
        width_1 = find_width(0.0001, L, k, V_OV_1, region_1)
        
        V_DS2 = 0.6 # volts
        V_GS2 = V_DS2 # volts

        region_2, V_OV_2 = find_region(V_DS2, V_GS2, V_TH)
        width_2 = find_width(0.0001, L, k, V_OV_2, region_2)

        # print results
        print(f"The region for Q2 is {region_1}. the width is {width_1* 10 ** 6: .3f}[um]")
        print(f"The region for Q1 is {region_2}. the width is {width_2* 10 ** 6: .3f}[um]")
        
        # exit gracefully
        return True

# begin gracefully
if __name__ == '__main__':
	main(sys.argv[0:])
        
# End of file
