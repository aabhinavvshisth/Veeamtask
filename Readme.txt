- Only works on folder level. It does not take into account the content of the files.
- Works one way from source to replica 
- The following parameters are expected from command line: 
    -s : path of the source folder
    -r : path of the replica folder
    -l : path where the log file should be created. The log file name will be synclog.txt. If the file already exists, the new entries will be added 
         after the existing ones. 
    -st : synchronization time interval in seconds. Default value is 100 seconds 
- Ctrl + C to stop the command 

