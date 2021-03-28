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
cmd = "ls"
x = execute_cmd(cmd)

```

### TO DO

- [x] execute shell commands

- [ ] saving and return outputs

- [ ] Logging of every command
