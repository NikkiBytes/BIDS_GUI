"""
Author: Nichollette Acosta @ NIBL UNC Chapel Hill

Module for BIDS Conversion GUI
This is a conversion script the GUI uses to run Heudiconv

"""

from __main__ import *

global STUDYNAME
global INPUTDIR
global OUTPUTDIR
global DICOMPATH
global MULTISESS

def setSTUDYNAME(x):
    STUDYNAME = x
    print(STUDYNAME)
def setINPUTDIR(x):
    INPUTDIR = x
def setOUTPUTDIR(x):
    OUTPUTDIR = x
def setDICOMPATH(x):
    DICOMPATH = x
def setMULTISESS(x):
    MULTISESS = x
def setHEURISTICFILE(x):
    HEURISTICFILE = x

def runConversion():
    print("STARTING CONVERSION")
    ##input bash script here

"""
def main():
    runConversion(STUDYNAME)

if __name__ == '__main__':
    main()
"""
