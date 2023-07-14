import shutil
import os
import time
import argparse

from timeloop import Timeloop
from datetime import timedelta

parser = argparse.ArgumentParser(description='Syncronize folder from Source to Replica')

parser.add_argument("-s","--source", help = 'path to source folder')
parser.add_argument("-r","--replica", help = 'path to replica folder')
parser.add_argument("-l","--logfile", help = 'path to sync log')
parser.add_argument("-st","--synctime", help = 'Folder Sync interval', type=int, default=100)

args = parser.parse_args()

source = args.source
replica = args.replica
logfileloc = args.logfile
synctimeperiod = args.synctime

#logfile name
logfilename = logfileloc+'\\synclog.txt'

#Timeloop
tl = Timeloop()

@tl.job(interval=timedelta(seconds=synctimeperiod))
def foldersync():
     ####comparing the file list in both folders
    source_filelist = os.listdir(source)
    replica_filelist = os.listdir(replica)

    source_filelist_set = set(source_filelist)
    replica_filelist_set = set(replica_filelist)

    addedfiles = source_filelist_set - replica_filelist_set
    deletedfiles = replica_filelist_set - source_filelist_set

    ## Operations
    ## Copy
    for filename in addedfiles:
        inputpath = os.path.join(source, filename)
        outputpath = os.path.join(replica, filename)
        shutil.copy2(inputpath, outputpath) ## copy the file
        
        current_time = time.ctime() ##reading the current time from system
        logfile = open(logfilename, "a+")
        logentry = current_time+' : '+filename+' is copied'
        logfile.write(str(logentry)+"\n")
        print(logentry)

    #delete
    for filename in deletedfiles:
        
        outputpath = os.path.join(replica, filename)
        
        os.remove(outputpath)
        
        current_time = time.ctime() ##reading the current time from system
        logfile = open(logfilename, "a+")
        logentry = current_time+' : '+filename+' is deleted'
        logfile.write(str(logentry)+"\n")
        print(logentry)


if __name__ == "__main__":
    tl.start(block=True)