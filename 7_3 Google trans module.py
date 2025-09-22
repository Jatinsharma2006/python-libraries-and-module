#pip install google trans

from googletrans import Translator

translator=Translator()

text=str(input("ENTER TEXT TO TRANSLATE:"))

translation=translator.translate(text,src="en",dest="hi")

print("Translated Text:",translation.text)
