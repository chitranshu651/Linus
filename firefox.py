import subprocess
from main import parameter

def open_url():
    subprocess.Popen("firefox -new-tab " + (parameter['url']), stdout=subprocess.PIPE, stdin=subprocess.PIPE, shell=True)
