import subprocess
import platform
import os
import sys
import io

def get_os_name()->str:
    """ Return os name as a string
    For windows -> 'Windows'  
    For Linux -> 'Linux' 
    For Mac -> 'Darwin'
    """
    return platform.system()

osname = get_os_name()
shell = True
outputfilename = "outputfile.txt"
cmd = "dir"

if osname == 'Linux':
    # cmd += ' 2>&1 | tee %s' %(outputfilename) # with tee command it doesn't throw error when unsuccessful;
    # so we are not manipulating command for now. and will see a workaround
    # cmdinstance = subprocess.run(cmd,shell=shell)
    # print('Tee command executed')

    ### applying same command execution for linux ###
    outputfile = open(outputfilename,'w') 
    cmdinstance = subprocess.run(cmd,shell=shell,stderr=outputfile,stdout=outputfile)
    outputfile.close()
else :
    outputfile = open(outputfilename,'w') 
    cmdinstance = subprocess.run(cmd,shell=shell,stderr=outputfile,stdout=outputfile)
    outputfile.close()




# io.open() is the preferred, higher-level interface to file I/O. 
# It wraps the OS-level file descriptor in an object that you can use to access the file in a Pythonic manner.

# os.open() is just a wrapper for the lower-level POSIX syscall. 
# It takes less symbolic (and more POSIX-y) arguments, and returns the file descriptor (a number) that represents the opened file. 
# It does not return a file object; the returned value will not have read() or write() methods.

# From the os.open() documentation:

#     This function is intended for low-level I/O. For normal usage, use the built-in function open(), which returns a “file object” with read() and write() methods (and many more).

