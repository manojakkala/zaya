import speech_recognition as sr
import os
from zaya import mainExe



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
    queery = Listen().lower()
    if 'wake up' in queery:
        print("Wakeup Detected")
        mainExe()
    else:
        pass    

while True:
    WakeupDetected()