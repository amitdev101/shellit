import subprocess,sys
def execute_cmd(cmd):
    subprocess.run(cmd)

def execute(command):
    fulloutput = ""
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

    # Poll process for new output until finished
    while True:
        nextline = process.stdout.readline()
        nextline = nextline.decode('utf-8')
        fulloutput+=nextline
        if nextline == '' and process.poll() is not None:
            break
        sys.stdout.write(nextline)
        # sys.stdout.write(nextline.decode('utf-8'))
        sys.stdout.flush()

    output = process.communicate()[0]
    exitCode = process.returncode

    output = fulloutput
    if (exitCode == 0):
        return output
    else:
        raise ProcessException(command, exitCode, output)


def execute_with_popen(cmd):
    output = ""
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE,stderr=subprocess.STDOUT, universal_newlines=True)
    for stdout_line in iter(process.stdout.readline, ""):
        output+=stdout_line
        print(stdout_line,end="")
        ## for now we don't use yield to yield every line output
        # yield stdout_line
    process.stdout.close()
    return_code = process.wait()
    return return_code, output
        

cmd = "python shellit/async_print_test.pya"

# execute_cmd(cmd)
# out = execute(cmd)
# for line in execute_with_popen(cmd):
#     print(line,end="")
x, output = execute_with_popen(cmd)
print("return code is ",x)
print("output is here ",output)