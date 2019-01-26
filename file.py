import requests


def fileio(parameter):
    files = {
        'file': (parameter['filePath'], open(parameter['filePath'], 'rb')),
    }
    response = requests.post('https://file.io/', files=files)
    if str(response.json()).split("'")[2].__contains__('True'):
        print(str(response.json()).split("'")[9])
    else:
        print('fail')
