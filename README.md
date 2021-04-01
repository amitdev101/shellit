# SHELLIT (shell it)

shellit(shell it) is a package that will easily let you run shell commands from python and return your outputs.

## Motivation

As a developer I need to run shell commands and check the output and based on the outputI make the decision.
So to help developers who just want to run some shell commands with python here is the simple module :)
Just install and run shell commands.

## Setup 

pip install shellit

```
from shellit import execute_cmd
outputfilename = 'shellit_output.txt'
cmd = "ls"
returncode, output = execute_cmd(cmd, shell=True, forced=False, outputfilename=outputfilename)

### Explaination ###

'''
    @param cmd(str) : cmd is a string which you want to execute with shell
    @param shell(bool) : shell is set to True to execute all commands in shell without any restrictions
    @param force(bool) : force to execute all commands even rm command.
    @param outputfilename(str) : name of the file in which output will be saved.
                              'shellit_output.txt' ($DEFAULT)  
    return 'returncode'(int) : 0 for successful.
                                any other num for unsuccessful command or if any error is thrown by the command.
            'output'(str) : An output string 
    '''

## console output ##

Executing cmd 'ls'
__init__.py
extra_feature_test
shellit.py
shellit_output.txt
cmd successful : 'ls'

## output finished ##

## Variable values ##
returncode = 0
output = "__init__.py\nextra_feature_test\nshellit.py\nshellit_output.txt"
##                 ##


returncode = 0 # Successful 
returncode !=0 # Unsuccessful



```

### TO DO

- [x] execute shell commands

- [x] saving and return outputs

- [x] Simultaneously printing and saving the output

- [ ] Testing on large output 
