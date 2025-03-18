# IMPORTATION
import numpy as NP

# DEFINITION
IDArray = 0

IIDArray = 0
IIDArrayN2 = 0

IIIDArray = 0
IIIDArrayN2 = 0

IVDArray = 0
IVDArrayN2 = 0

# MANIPULATION
IDArray = NP.arange(0, 15, 1)

IIDArray = NP.arange(0, 15, 1)
IIDArray = IIDArray.reshape(3, 5)

IIDArrayN2 = NP.arange(0, 15, 1).reshape(3, 5)

IIIDArray = NP.arange(0, 15, 1).reshape(5, 3, 1)

IIIDArrayN2 = NP.arange(0, 30, 1).reshape(5, 3, 2)

IVDArray = NP.arange(0, 15, 1).reshape(3, 1, 1, 5)

IVDArrayN2 = NP.arange(0, 60, 1).reshape(3, 2, 2, 5)

# REPRESENTAION
print("\nIDArray: ", IDArray)
print("\n------------------------------------------------------")

print("\nIIDArray: ", IIDArray)
print("\n------------------------------------------------------")

print("\nIIDArrayN2: ", IIDArrayN2)
print("\n------------------------------------------------------")

print("\nIIIDArray: ", IIIDArray)
print("\n------------------------------------------------------")

print("\nIIIDArrayN2: ", IIIDArrayN2)
print("\n------------------------------------------------------")

print("\nIVDArray: ", IVDArray)
print("\n------------------------------------------------------")

print("\nIVDArrayN2: ", IVDArrayN2)