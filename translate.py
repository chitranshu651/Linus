import json

from googletrans import Translator

def translate(parameter):
    translator = Translator()
    ans =translator.translate(parameter['query'], dest=parameter['langauge'])
    print(ans.text)
    file = open('/home/iosdev747/Desktop/Linus/Linus/output.txt', 'w')

    data = {}
    order = []
    Image = []
    URI = []
    Text = []
    order.append(3)
    Text.append({"data":ans.text})
    data['title'] = 'translation of ' + parameter['query']
    data['order'] = order
    data['Image'] = Image
    data['URI'] = URI
    data['Text'] = Text
    data['command'] = ""
    json_data = json.dumps(data)
    file.write(json_data)
    file.close()
