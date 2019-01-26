import json
from urllib.parse import quote
from urllib.request import urlopen
import xml.etree.ElementTree as ET
import firefox


def wolfram(parameter):
    from credentials import app_id
    url = "http://api.wolframalpha.com/v2/query?input="+parameter['query'].replace(" ","+").replace("#","+")+"&appid="+app_id
    xml_data = urlopen(url).read()
    root = ET.fromstring(xml_data)
    title = parameter['query']
    order = []
    Image = []
    URI = []
    Text = []
    print('url: ' + url)
    print("----"*10)
    for pod in root.findall('pod'):
        print('-------------------------------------------\n\n')
        print(str(pod.attrib).split("'")[3])
        Text.append({"data": str(pod.attrib).split("'")[3]})
        order.append(3)
        for img in pod.iter('img'):
            print(str(img.attrib).split("'")[3])
            Image.append({"src": str(img.attrib).split("'")[3],"placeHolder":'#'})
            order.append(1)
    Text.append({"data":"Powered by the Wolfram Language"})
    order.append(3)
    file = open('/home/iosdev747/Desktop/Linus/Linus/output.txt', 'w')
    data = {}
    data['title'] = title.replace('+', ' ')
    data['order'] = order
    data['Image'] = Image
    data['URI'] = URI
    data['Text'] = Text
    data['command'] = ""
    json_data = json.dumps(data)
    file.write(json_data)
    exit(0)


def google(parameter):
    parameter['search-string'] = parameter['search-string'].replace("#"," ")
    if parameter['search-engine'] == 'Google':
        parameter['url'] = 'https://google.com/search?q=' + quote(parameter['search-string'])
    elif parameter['search-engine'] == 'Wikipedia':
        parameter['url'] = 'https://en.wikipedia.org/wiki/' + quote(parameter['search-string'])
    elif parameter['search-engine'] == 'Amazon':
        parameter['url'] = 'https://www.amazon.in/s/?field-keywords=' + quote(parameter['search-string'])
    elif parameter['search-engine'] == 'DuckDuckGo':
        parameter['url'] = 'https://duckduckgo.com/?q=' + quote(parameter['search-string'])
    elif parameter['search-engine'] == 'Bing':
        parameter['url'] = 'https://bing.com/search?q=' + quote(parameter['search-string'])
    elif parameter['search-engine'] == 'Stackoverflow':
        parameter['url'] = 'https://stackoverflow.com/search?q=' + quote(parameter['search-string'])
    else:
        parameter['url'] = 'wolfram'
        parameter['query'] = parameter['search-string']
    print(parameter['url'])
    if not parameter['url'] == 'wolfram':
        firefox.open_url(parameter)
    else:
        wolfram(parameter)
