import json
import sys
from urllib.parse import quote
import command
import firefox
import file
import search
import translate


def parameter_error():
    print('Insufficient Parameter Specified')
    exit(0)


# noinspection PyStatementEffect
def debug():
    pass


def build_json(action,cmd,str):
    file = open('output', 'w')
    data = {}
    order = []
    Image = []
    URI = []
    Text = []
    order.append(3)
    Text.append(Text.append({"data": str}))
    data['title'] = action
    data['order'] = order
    data['Image'] = Image
    data['URI'] = URI
    data['Text'] = Text
    data['command'] = cmd
    json_data = json.dumps(data)
    file.write(json_data)
    file.close()


def main():
    arguments = sys.argv[1:]
    print(arguments)
    action = arguments[0]
    arguments[1] = arguments[1].replace("desktop","Desktop").replace("downloads","Downloads").replace("music","Music")
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
        parameter['absSrcPath'] = '/'+parameter['absSrcPath'].replace("#","/")
        parameter['absDestPath'] = '/'+parameter['absDestPath'].replace("#","/")+'/'
        parameter['command'] = 'cp ' + parameter['absSrcPath'] + '/' + parameter['fileName'] + ' ' + parameter[
            'absDestPath']
        print('::cp::')
        print(parameter['command'])
        build_json("Command is Being Executed",parameter['command'],command.execute_command(parameter))
    elif action == 'devdocs':
        try:
            parameter['query']
        except KeyError:
            parameter_error()
        parameter['url'] = 'devdocs.io/search?q=' + quote(parameter['query'].replace("#","+"))
        print('::devdocs::')
        print(parameter['url'])
        firefox.open_url(parameter)

    elif action == 'cmd':
        try:
            parameter['command']
        except KeyError:
            parameter_error()
        print('::cmd::')
        parameter['command'] = parameter['command'].replace("#"," ")
        print(parameter['command'])
        build_json("Command is Being Executed",parameter['command'],command.execute_command(parameter))

    elif action == 'ps':
        print('::ps::')
        parameter['command'] = 'ps -x | grep pts'
        print(parameter['command'])
        build_json("Command is Being Executed", parameter['command'], command.execute_command(parameter))

    elif action == 'kill':
        try:
            parameter['pid']
        except KeyError:
            parameter_error()
        parameter['command'] = 'kill -9 ' + parameter['pid']
        print('::kill::')
        print(parameter['command'])
        command.execute_command(parameter)
        build_json("Killed " + parameter['pid'] + " process.", parameter['command'], "")
    elif action == 'man':
        try:
            parameter['command']
        except KeyError:
            parameter_error()
        parameter['command'] = 'man ' + parameter['command'] + '| cat'
        print('::man::')
        print(parameter['command'])
        build_json("Here is what I found", parameter['command'], command.execute_command(parameter))

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
        parameter['absSrcPath'] = '/' + parameter['absSrcPath'].replace("#", "/")
        parameter['absDestPath'] = '/' + parameter['absDestPath'].replace("#", "/") + '/'
        parameter['command'] = 'mv ' + parameter['absSrcPath'] + '/' + parameter['fileName'] + ' ' + parameter['absDestPath']
        print('::mv::')
        print(parameter['command'])
        build_json("Command is Being Executed", parameter['command'], command.execute_command(parameter))

    elif action == 'rmdir':
        try:
            parameter['absPath']
            parameter['pwd']
            parameter['directoryName']
        except KeyError:
            parameter_error()
        if parameter['absPath'] == "":
            parameter['absPath'] = parameter['pwd']
        parameter['absPath'] = '/'+parameter['absPath'].replace("#","/")+'/'
        parameter['command'] = 'rm -r ' + parameter['absPath'] + parameter['directoryName']
        print('::rmdir::')
        print(parameter['command'])
        build_json("Command is Being Executed", parameter['command'], command.execute_command(parameter))

    elif action == 'rm':
        try:
            parameter['absPath']
            parameter['pwd']
            parameter['fileName']
        except KeyError:
            parameter_error()
        if parameter['absPath'] == "":
            parameter['absPath'] = parameter['pwd']
        parameter['absPath'] = '/'+parameter['absPath'].replace("#","/")+'/'
        parameter['command'] = 'rm ' + parameter['absPath'] + parameter['fileName']
        print('::rm::')
        print(parameter['command'])
        build_json("Command is Being Executed", parameter['command'], command.execute_command(parameter))

    elif action == 'ls':
        try:
            parameter['pwd']
            parameter['path']
        except KeyError:
            parameter_error()
        print('::ls::')
        print(parameter['pwd'])
        print(parameter['path'])
        parameter['command'] = 'ls /' + parameter['pwd'].replace("#","/") + '/' + parameter['path'].replace("#"," ")
        print(parameter['command'])
        build_json("Command is Being Executed", parameter['command'], command.execute_command(parameter))

    elif action == 'htop':
        print('::htop::')
        parameter['command'] = "top -n 1 -b"
        build_json("Command is Being Executed", parameter['command'], command.execute_command(parameter))

    elif action == 'whatis':
        try:
            parameter['command']
        except KeyError:
            parameter_error()
        parameter['command'] = 'whatis ' + parameter['command']
        build_json("Command is Being Executed", parameter['command'], command.execute_command(parameter))

    elif action == 'loadFirefox':
        try:
            parameter['saveFile']
        except KeyError:
            parameter_error()
        print('::loadFirefox::')
        print(parameter['saveFile'])
        firefox.load(parameter)
        build_json("Loading " + parameter['saveFile'] + "Firefox State", "", "")

    elif action == 'showFirefox':
        print('::showFirefox::')
        firefox.show(parameter)

    elif action == 'saveFirefox':
        try:
            parameter['saveFile']
        except KeyError:
            parameter_error()
        print('::saveFirefox::')
        print(parameter['saveFile'])
        build_json("Loading" + parameter['saveFile'] + "Firefox State", "", "")
        firefox.save(parameter)

    elif action == 'url':
        try:
            parameter['url']
        except KeyError:
            parameter_error()
        print('::url::')
        print(parameter['url'])
        firefox.open_url(parameter)
        build_json("Opened " + parameter['url'], "", "")

    elif action == 'fileio':
        try:
            parameter['pwd']
            parameter['filePath']
        except KeyError:
            parameter_error()
        print('::fileio::')
        parameter['filePath'] = '/'+parameter['pwd'].replace("#","/")+'/'+parameter['filePath'].replace("#","/")
        print(parameter['filePath'])
        file.fileio(parameter)
        build_json("File Sharing Link " , "", parameter['result'])

    elif action == "fsearch":
        try:
            parameter['key']
        except KeyError:
            parameter_error()
        parameter['command'] = "locate " + parameter['key'].replace('#', '\ ')
        print('::fsearch::')
        print(parameter['command'])
        build_json(action, parameter['command'], command.execute_command(parameter))

    elif action == "gsearch":
        try:
            parameter['search_string']
            parameter['search_engine']
        except KeyError:
            parameter_error()
        print('::gsearch::')
        search.google(parameter)
        if not parameter['url'] == 'wolfram':
            build_json("Opened", "", parameter['url'])

    elif action == 'wsearch':
        try:
            parameter['query']
        except KeyError:
            parameter_error()
        print('::wolfsearch::')
        print(parameter['query'])
        search.wolfram(parameter)

    elif action == 'translate':
        try:
            parameter['query']
            parameter['langauge']
        except KeyError:
            parameter_error()
        print('::translate::')
        print(parameter['query'])
        print(parameter['langauge'])
        translate.translate(parameter)

    elif action == 'weather':
        try:
            parameter['location']
        except KeyError:
            parameter_error()
        print('::weather::')
        print(parameter['location'])
        parameter['query'] = 'weather+at+' + parameter['location'].replace(" ","+").replace("#","+")
        search.wolfram(parameter)

    elif action == 'dictionary':
        try:
            parameter['word']
        except KeyError:
            parameter_error()
        parameter['query'] = 'meaning+of+' + parameter['word'].replace(" ","+").replace("#","+")
        print('::dictionary::')
        print(parameter['query'])
        search.wolfram(parameter)
    elif action == 'debug':
        debug()
    else:
        print('Undefined Action')


if __name__ == '__main__':
    main()

