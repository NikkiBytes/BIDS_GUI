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
    global SUBJECTS
    global IDS 
    IDS = []
    SUBJECTS = []
    for sub in x:
        _id = sub.split("-")[1]
        _id = round(int(_id)/1) 
        SUBJECTS.append(_id)
    IDS = sorted(IDS)
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
    
    if MULTISESS == False:
        BIDS_CMD = "singularity exec -B /:/test /projects/niblab/bids_projects/Singularity_Containers/heudiconv.simg heudiconv -d %s -s SUBJECT -f dcm2niix -c %s -o %s/SUBJECT"%(INPUTPATH, HEURISTICFILE, OUTPUTDIR)
    else:
        BIDS_CMD = "singularity exec -B /:/test /projects/niblab/bids_projects/Singularity_Containers/heudiconv.simg heudiconv -d %s -s SUBJECT -ss %s -f dcm2niix -c %s -o %s/SUBJECT"%(INPUTPATH, SESS_ID,  HEURISTICFILE, OUTPUTDIR)


    
    """def divide_chunks(l, n): 
    # looping till length l 
        for i in range(0, len(l), n):  
            yield l[i:i + n] 
    """
    
    
    SUB_COUNT = len(IDS)
    if SUB_COUNT > 100:
        BATCH_SPLIT = 10
        JOB_SPLIT = 50
    elif SUB_COUNT > 50:
        BATCH_SPLIT = 5
        JOB_SPLIT = 30
    elif SUB_COUNT > 20:
        BATCH_SPLIT = 3
        JOB_SPLIT = 20
    elif SUB_COUNT > 10:
        BATCH_SPLIT = 2
        JOB_SPLIT = 10
    else: 
        BATCH_SPLIT = 1
        JOB_SPLIT = 5
    
    start=SUBJECTS[0]
    finish=SUBJECTS[-1]
    BATCH_CMD = "sbatch --array=%s-%s"%(start,finish)+"%"+"%s /Users/nikkibytes/Documents/GUIS/BIDS_GUI/run_bids.job"%(JOB_SPLIT)
    #print(BATCH_CMD)
    INPUT = os.path.join(INPUTPATH, "*."+DICOM)

    run_batch = subprocess.Popen(["/Users/nikkibytes/Documents/GUIS/BIDS_GUI/test.sh", BIDS_CMD])
    
    
    
    #batches = list(divide_chunks(SUBJECTS, round(SUB_COUNT/BATCH_SPLIT))) 
    """for _list in batches:
        y = len(_list)
        start = _list[0]
        finish = _list[-1]
        BATCH_CMD = "sbatch --array=%s-%s"%(start,finish)+"%"+"%s /projects/wherereverIputit/run_bids.job"%(y)
        print(BATCH_CMD)"""
    
#run_batch=subprocess.Popen(["sbatch /projects/niblab/bids_projects/Heudiconv_drypass/drypass.job", heudiconv_cmd])