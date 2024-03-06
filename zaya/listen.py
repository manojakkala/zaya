import speech_recognition as sr
from googletrans import Translator


#listen function

def Listen():
    r = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("Say Something")
        r.pause_threshold = 1
        audio = r.listen(source,0,5) #listening mode
        print("Done Listening")
    try:
        print("Recognizing")
        #query = r.recognize_google(audio, language='hi')
        query = r.recognize_google(audio, language='en')
    except:
        print("Say that again please...")
        return "None"

    query = str(query).lower()
    return query

#translate

def TranslationHintoEng(Text):
    line = str(Text)
    translator = Translator()
    translated = translator.translate(Text, src='hi', dest='en')

    print(f"Translated Text: {translated.text}")
    return translated.text

def TranslationTeltoEng(Text):
    line = str(Text)
    translator = Translator()
    translated = translator.translate(Text, src='te', dest='en')

    print(f"Translated Text: {translated.text}")
    return translated.text

#connect
'''
def MicExcecution():
    query = Listen()
    if 'none' in query:
        return
    else:
        #data = TranslationHintoEng(query)
        data = TranslationTeltoEng(query)
'''

def MicExcecution():
    query = Listen()
    if 'none' in query:
        return
    else:
        data = query
        return data