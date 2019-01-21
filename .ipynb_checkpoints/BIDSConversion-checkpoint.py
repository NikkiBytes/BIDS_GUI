"""
Author: Nichollette Acosta @ NIBL UNC Chapel Hill

Module for BIDS Conversion GUI
This is a conversion script the GUI uses to run Heudiconv


## NEED TO MODIFY FOR MULTI SESSIONS
## NEED TO ADD ERROR FILE OUTPUT 
## NEED TO TEST 
"""

from __main__ import *
import os, subprocess

def setINPUTDIR(x):
    global INPUTPATH
    INPUTPATH = "/test" + x + "/{subject}"
def setSUBJECTS(x):
    global SUBJ_STRING
    SUBJ_STRING = " ".join(x)
def setOUTPUTDIR(x):
    global OUTPUTDIR
    OUTPUTDIR = "/test" + x
def setDICOM(x):
    global DICOM
    DICOM = x
def setMULTISESS(x):
    global MULTISESS
    MULTISESS = x
def setSESSIONID(x):
    global SESS_ID
    SESS_ID = x
def setHEURISTICFILE(x):
    global HEURISTICFILE
    HEURISTICFILE = "/test" + x

def runConversion():
    #print(SUBJ_STRING)
    INPUT = INPUTPATH+"/*%s"%(DICOM)
    if MULTISESS == False:
        BIDS_CMD = "singularity exec -B /:/test /projects/niblab/bids_projects/Singularity_Containers/heudiconv.simg heudiconv -d %s -s %s -f dcm2niix -c %s -o %s"%(INPUT, SUBJ_STRING, HEURISTICFILE, OUTPUTDIR)
    else:
        OUTPUT = OUTPUTDIR+"/ses-%s"%(SESS_ID)
        BIDS_CMD = "singularity exec -B /:/test /projects/niblab/bids_projects/Singularity_Containers/heudiconv.simg heudiconv -d %s -s %s -ss %s -f dcm2niix -c %s -o %s"%(INPUT, SUBJ_STRING, SESS_ID,  HEURISTICFILE, OUTPUT)
    #BATCH_CMD = "sbatch --array=%s-%s"%(start,finish)+"%"+"%s /Users/nikkibytes/Documents/GUIS/BIDS_GUI/run_bids.job"%(JOB_SPLIT)
    run_batch = subprocess.Popen([BATCH_CMD, BIDS_CMD])
    
    
    
