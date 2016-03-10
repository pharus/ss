#!/usr/bin/python3

#
# computing musical notes
# A4 -> 440 Hz
# 
# Compute G4, G#4, B4, and C5

A4 = 440

#
# computeFreq, computes frequencie of a given note, by giving its relative
# position to A4 in halftones
#
def computeFreq(dist):
    base = 2**(1/12) # distance between each half tone
    return A4 * base ** dist

G4 = computeFreq(-2)
GS4 = computeFreq(-1) # G# => GS
B4 = computeFreq(2)
C5 = computeFreq(3)

print("G4  = %3.3f Hz" % G4)
print("G#4 = %3.3f Hz" % GS4)
print("B4  = %3.3f Hz" % B4)
print("C5  = %3.3f Hz" % C5)

