import speech_recognition as sr
import os


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
        print(f"User said: {query}\n")
    except:
        print("Say that again please...")
        return "None"

    query = str(query).lower()
    print(query)
    return query

def WakeupDetected():
    query = Listen().lower()
    if 'wake up' in query:
        os.startfile(r"D:\projects\ai projects\zaya 3\main.py")
    else:
        pass    

while True:
    WakeupDetected()