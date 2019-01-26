import json
from urllib.request import urlopen
import xml.etree.ElementTree as ET

def wolfram(parameter):
    from credentials import app_id
    url = "http://api.wolframalpha.com/v2/query?input="+parameter['query']+"&appid="+app_id
    xml_data = urlopen(url).read()
    root = ET.fromstring(xml_data)
    title = parameter['query']
    order = []
    Image = []
    URI = []
    Text = []
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
    #make json for printing output
    file = open('output', 'w')
    data = {}
    data['title'] = title
    data['order'] = order
    data['Image'] = Image
    data['URI'] = URI
    data['Text'] = Text
    json_data = json.dumps(data)
    file.write(json_data)
    exit(0)