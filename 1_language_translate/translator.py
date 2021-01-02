# pip install googletrans==3.1.0a0

from googletrans import Translator
translator = Translator()

out = translator.translate("क्या हाल है", dest='en')
print(out)

mystory = '''Tell me who doesn't love baby yoda from mandolarian? 
Baby yoda has shaken me like soda.
'''
out = translator.translate(mystory, dest='hi')
print(out.text)

out = translator.translate("I am learning python", dest='gu')
print(out)
