import sys
from urllib.parse import quote
import command
import firefox

def parameter_error():
    print('Insufficient Parameter Specified')
    exit(0)


# noinspection PyStatementEffect
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

    if action == 'cp':
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

    elif action == 'apropos':
        try:
            parameter['command']
        except KeyError:
            parameter_error()
        parameter['command'] = 'apropos ' + parameter['command']
        print('::apropos::')
        print(parameter['command'])
        command.execute_command(parameter)
    elif action == 'cmd':
        try:
            parameter['command']
        except KeyError:
            parameter_error()
        print('::cmd::')
        print(parameter['command'])
        command.execute_command(parameter)
    elif action == 'kill':
        try:
            parameter['pid']
        except KeyError:
            parameter_error()
        parameter['command'] = 'kill -9 ' + parameter['pid']
        print('::kill::')
        print(parameter['command'])
        command.execute_command(parameter)
    elif action == 'man':
        try:
            parameter['command']
        except KeyError:
            parameter_error()
        parameter['command'] = 'man ' + parameter['command'] + '| cat'
        print('::man::')
        print(parameter['command'])
        command.execute_command(parameter)
    elif action == 'move':
        try:
            parameter['absSrcPath']
            parameter['pwd']
            parameter['fileName']
            parameter['absDestPath']
        except KeyError:
            parameter_error()
        if parameter['absSrcPath'] == '':
            parameter['absSrcPath'] = parameter['pwd']
        parameter['command'] = 'mv ' + parameter['absSrcPath'] + '/' + parameter['fileName'] + ' ' + parameter['absDestPath']
        print('::mv::')
        print(parameter['command'])
        command.execute_command(parameter)
    elif action == 'rmdir':
        try:
            parameter['absPath']
            parameter['pwd']
            parameter['directoryName']
        except KeyError:
            parameter_error()
        parameter['command'] = 'rm -r ' + parameter['pwd'] + parameter['absPath'] + parameter['directoryName']
        print('::rmdir::')
        print(parameter['command'])
        command.execute_command(parameter)
    elif action == 'rm':
        try:
            parameter['absSrcPath']
            parameter['pwd']
            parameter['fileName']
        except KeyError:
            parameter_error()
        parameter['command'] = 'rm ' + parameter['pwd'] + parameter['absPath'] + parameter['fileName']
        print('::rm::')
        print(parameter['command'])
        command.execute_command(parameter)
    elif action == 'ls':
        try:
            parameter['pwd']
            parameter['path']
        except KeyError:
            parameter_error()
        print('::ls::')
        print(parameter['pwd'])
        print(parameter['path'])
        parameter['command'] = 'ls ' + parameter['pwd'] + '/' + parameter['path']
        command.execute_command(parameter)
    elif action == 'htop':
        print('::htop::')
        parameter['command'] = "top -n 1 -b"
        command.execute_command(parameter)
    elif action == 'whatis':
        try:
            parameter['command']
        except KeyError:
            parameter_error()
        parameter['command'] = 'whatis ' + parameter['command']
        command.execute_command(parameter)
    else:
        print('Undefined Action')


if __name__ == '__main__':
    main()
