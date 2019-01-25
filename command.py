import os
import subprocess


def execute_command(parameter):
    with open("output.data", "w") as outfile, open("error.data", "w") as errfile:
        subprocess.call(parameter['command'], shell=True, stdout=outfile, stderr=errfile)
    with open("output.data", "r") as outfile, open("error.data", "r") as errfile:
        if errfile.read():
            return "Error occurred"
        return outfile.read()


'''
It takes sudo passoword using environment variable "password"
'''
def sudo_execute_command(parameter):
    with open("output.data", "w") as outfile, open("error.data", "w") as errfile:
        p = subprocess.Popen('sudo -S' + parameter['command'], shell=True, stdout=outfile, stderr=errfile)
        sudo_prompt = p.communicate(os.environ['password'] + '\n')[1]
    with open("output.data", "r") as outfile, open("error.data", "r") as errfile:
        if errfile.read():
            return "Error occurred"

        return outfile.read()
