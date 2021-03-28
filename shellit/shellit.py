import subprocess

def execute_cmd(cmd:str, shell:bool=True, forced:bool=False)->int:
    '''
    @param cmd(str) : cmd is a string which you want to execute with shell
    @param shell(bool) : shell is set to True to execute all commands in shell without any restrictions
    @param force(bool) : force to execute all commands even rm command.
    return 'returncode'(int) : 0 for successful.
                                any other num for unsuccessful command or if any error is thrown by the command.
    '''
    print("Executing cmd '%s'" %(cmd))
    returncode = -1
    ### safety code ###
    if not forced :
        restricted_cmds = ('rm',) # add your restricted cmds
        words = cmd.split(' ')
        for word in words :
            if word in restricted_cmds :
                print("'%s' word is restricted. Hence can't execute the following cmd '%s'" %(word,cmd))
                print("To execute the restricted cmd. Pass 'force=True' in execute_cmd function")
                return returncode
    #######################
    cmdinstance = subprocess.run(cmd,shell=shell)
    returncode = cmdinstance.returncode
    if returncode == 0:
        print("cmd successful : '%s'" %(cmd))
    else :
        print("Unsuccessful cmd : '%s'" %(cmd))
    return returncode

if __name__=='__main__':
    cmd = 'rm dir'
    x = execute_cmd(cmd)
    print(x)
