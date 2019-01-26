from googletrans import Translator

def translate(parameter):
    translator = Translator()
    ans =translator.translate(parameter['query'], dest=parameter['language'])
    print(ans.text)
