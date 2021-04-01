import subprocess
import platform
import os
import sys

def get_os_name()->str:
    """ Return os name as a string
    For windows -> 'Windows'  
    For Linux -> 'Linux' 
    For Mac -> 'Darwin'
    """
    return platform.system()

def execute_cmd(cmd:str, 
                shell:bool=True, 
                forced:bool=False,
                outputfilename:str='shellit_output.txt',
                )->int:
    '''
    @param cmd(str) : cmd is a string which you want to execute with shell
    @param shell(bool) : shell is set to True to execute all commands in shell without any restrictions
    @param force(bool) : force to execute all commands even rm command.
    @param outputfilename(str) : name of the file in which output will be saved.
    return 'returncode'(int) : 0 for successful.
                                any other num for unsuccessful command or if any error is thrown by the command.
            'output'(str) : An output string 
    '''
    print("Executing cmd '%s'" %(cmd))

    # initializing return code
    returncode = -1 
    ### safety code ###
    if not forced :
        restricted_cmds = ('rm',) # add your restricted cmds
        words = cmd.split(' ')
        for word in words :
            if word in restricted_cmds :
                print("'%s' word is restricted. Hence can't execute the following cmd '%s'" %(word,cmd))
                print("To execute the restricted cmd. Pass 'forced=True' in execute_cmd function")
                return returncode
    #######################

    output = ""
    process = subprocess.Popen(cmd,shell=shell, stdout=subprocess.PIPE,stderr=subprocess.STDOUT, universal_newlines=True)
    for stdout_line in iter(process.stdout.readline, ""):
        output+=stdout_line # adding every line to output
        print(stdout_line,end="")
        ## for now we don't use yield to yield every line output
        # yield stdout_line
    process.stdout.close()
    returncode = process.wait()
    
    # Saving output to a file
    with open(outputfilename,'w') as f:
        f.write(output)
        f.close()

    if returncode == 0:
        print("cmd successful : '%s'" %(cmd))
    else :
        print("Unsuccessful cmd : '%s'" %(cmd))
    return returncode,output


if __name__=='__main__':
    osname = get_os_name()
    if osname == 'Windows':
        # cmd = 'dir'
        cmd = "python shellit/extra_feature_test/async_print_test.py"
    else :
        cmd = 'ls'
        # cmd = "python extra_feature_test/async_print_test.py"
    # wrong cmd executing by adding any variable say 'a'
    # cmd+='aaaaaaaaaaaaaaaa' # surely this won't exist
    
    x,output = execute_cmd(cmd)
    print(x)
    print(output)
    
