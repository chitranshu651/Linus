from googletrans import Translator

translator = Translator()
ans =translator.translate(parameter['query'], dest=parameter['language'])
print(ans.text)
