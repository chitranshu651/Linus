import json

from googletrans import Translator

def translate(parameter):
    translator = Translator()
    ans =translator.translate(parameter['query'], dest=parameter['language'])
    print(ans.text)
    file = open('output', 'w')
    data = {}
    order = []
    Image = []
    URI = []
    Text = []
    order.append(3)
    Text.append(ans.text)
    data['title'] = 'translation of ' + parameter['query']
    data['order'] = order
    data['Image'] = Image
    data['URI'] = URI
    data['Text'] = Text
    data['command'] = ""
    json_data = json.dumps(data)
    file.write(json_data)
    file.close()
