import requests


def fileio(parameter):
    files = {
        'file': (parameter['file'], open(parameter['file'], 'rb')),
    }
    response = requests.post('https://file.io/', files=files)
    if str(response.json()).split("'")[2].__contains__('True'):
        print(str(response.json()).split("'")[9])
    else:
        print('fail')
