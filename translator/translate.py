from googletrans import Translator

def translate(text):
    translator = Translator() #create instance
    translation = translator.translate(text=text, dest='de') 
    return translation.text