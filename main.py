import sys
from urllib.parse import quote
import command
import firefox

def parameter_error():
    print('Insufficient Parameter Specified')
    exit(0)


def main():
    arguments = sys.argv[1:]
    print(arguments)
    action = arguments[0]
    parameter = {}
    try:
        parameter = dict(item.split(":") for item in arguments[1].split(","))
    except:
        print('parameter is empty')
        print('Usage: python main.py action parameter1:value1,parameter2:value2...')
        exit(0)
    print(action)
    print(parameter)

    if action == 'cp':  # todo create empty file 'touch filename'
        try:
            parameter['absSrcPath']
            parameter['absDestPath']
            parameter['fileName']
            parameter['pwd']
        except KeyError:
            parameter_error()
        if parameter['absSrcPath'] == '':
            parameter['absSrcPath'] = parameter['pwd']
        parameter['command'] = 'cp ' + parameter['absSrcPath'] + '/' + parameter['fileName'] + ' ' + parameter[
            'absDestPath']
        print('::cp::')
        print(parameter['command'])
        command.execute_command(parameter)
    elif action == 'devdocs':
        try:
            parameter['query']
        except KeyError:
            parameter_error()
        parameter['url'] = 'devdocs.io/search?q=' + quote(parameter['query'])
        print('::devdocs::')
        print(parameter['url'])
        firefox.open_url(parameter)
    else:
        print('Undefined Action')


if __name__ == '__main__':
    main()
