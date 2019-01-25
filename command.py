import subprocess


def execute_command(parameter):
    with open("output.data", "w") as outfile, open("error.data", "w") as errfile:
        # subprocess.call("TERM=xterm top -n 1 -b", shell=True, stdout=outfile)
        subprocess.call(parameter['command'], shell=True, stdout=outfile, stderr=errfile)
    with open("output.data", "r") as outfile, open("error.data", "r") as errfile:
        if errfile.read():
            return ":-("
        return outfile.read()