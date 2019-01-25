import subprocess


def open_url(parameter):
    subprocess.Popen("firefox -new-tab " + (parameter['url']), stdout=subprocess.PIPE, stdin=subprocess.PIPE, shell=True)
