import os
import subprocess


def execute_command(parameter):
    with open("/home/iosdev747/Desktop/Linus/Linus/output.data", "w+") as outfile, open("/home/iosdev747/Desktop/Linus/Linus/error.data", "w+") as errfile:
        subprocess.call(parameter['command'], shell=True, stdout=outfile, stderr=errfile)
    with open("/home/iosdev747/Desktop/Linus/Linus/output.data", "r+") as outfile, open("/home/iosdev747/Desktop/Linus/Linus/error.data", "r+") as errfile:
        if errfile.read():
            return "Error occurred"

        return outfile.read()

'''
It takes sudo passoword using environment variable "password"
'''
def sudo_execute_command(parameter):
    with open("/home/iosdev747/Desktop/Linus/Linus/output.data", "w+") as outfile, open("/home/iosdev747/Desktop/Linus/Linus/error.data", "w+") as errfile:
        p = subprocess.Popen('sudo -S' + parameter['command'], shell=True, stdout=outfile, stderr=errfile)
        sudo_prompt = p.communicate(os.environ['password'] + '\n')[1]
    with open("/home/iosdev747/Desktop/Linus/Linus/output.data", "r+") as outfile, open("/home/iosdev747/Desktop/Linus/Linus/error.data", "r+") as errfile:
        if errfile.read():
            return "Error occurred"

        return outfile.read()
