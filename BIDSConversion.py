"""
Author: Nichollette Acosta @ NIBL UNC Chapel Hill

Module for BIDS Conversion GUI
This is a conversion script the GUI uses to run Heudiconv

"""

from __main__ import *

def setSTUDYNAME(x):
    global STUDYNAME
    STUDYNAME = x
def setSUBJECTS(x):
    global SUBJECTS
    SUBJECTS = sorted(x)
def setOUTPUTDIR(x):
    global OUTPUTDIR
    OUTPUTDIR = x
def setDICOMPATH(x):
    global DICOMPATH
    DICOMPATH = x
def setMULTISESS(x):
    global MULTISESS
    MULTISESS = x
def setSESSIONID(x):
    global SESS_ID
    SESS_ID = x
def setHEURISTICFILE(x):
    global HEURISTICFILE
    HEURISTICFILE = x

def runConversion():
    print(">>>>---------------------------> STARTING CONVERSION")
    
    if MULTISESS == False:
        print(">>>>----------------> HERE ARE MY VARIABLES: \n STUDYNAME:%s \nOUTPUTDIR:%s \nDICOMPATH:%s \
                \nMULTISESS:%s \nHEURISTICFILE:%s "%(STUDYNAME, OUTPUTDIR, DICOMPATH, MULTISESS, HEURISTICFILE))
        print(SUBJECTS)
        #bids_command = "singularity exec -B %s:/test %s heudiconv -b -d %s -s %s -f %s -c dcm2niix -b -o %s/{addsubject}"
        
    else:
            print(">>>>----------------> HERE ARE MY VARIABLES: \n STUDYNAME:%s \nINPUTDIR:%s \nOUTPUTDIR:%s \nDICOMPATH:%s \
                \nMULTISESS:%s \nHEURISTICFILE:%s \nSESS ID:%s"%(STUDYNAME, INPUTDIR, OUTPUTDIR, DICOMPATH, MULTISESS, HEURISTICFILE, SESS_ID))
        #bids_command = "singularity exec -B %s:/test %s heudiconv -b -d %s -s -ss %s -f %s -c dcm2niix -b -o %s/{addsubject}"
        #print(bids_command)

    
    def divide_chunks(l, n): 
    # looping till length l 
        for i in range(0, len(l), n):  
            yield l[i:i + n] 

        
    ##input bash script here
    GREATEST_SUB = SUBJECTS[-1].split("-")[1]
    SUB_COUNT = len(SUBJECTS)
    if SUB_COUNT > 100:
        BATCH_SPLIT = 10
    elif SUB_COUNT > 50:
        BATCH_SPLIT = 5 
    elif SUB_COUNT > 20:
        BATCH_SPLIT = 3
    elif SUB_COUNT > 10:
        BATCH_SPLIT = 2
    else: 
        BATCH_SPLIT = 1
    
    
    
    x = list(divide_chunks(SUBJECTS, round(SUB_COUNT/BATCH_SPLIT))) 
    for index, _list in enumerate(x):
        new_list = []
        for sub in _list:
            _id = sub.split("-")[1]
            _id = int(_id)/1 
            new_list.append(round(_id))
            x[index]= new_list
    print(x)
    #print(x)
#BATCH_CMD = #PUT BATCH COMMAND HERE
#run_batch=subprocess.Popen(["sbatch /projects/niblab/bids_projects/Heudiconv_drypass/drypass.job", heudiconv_cmd])