from brain.brain import replaybrain
from body.listen import MicExecution
print(">> starting zaya : wait for some time. ")
from body.speak import Speak
from features.clap import Tester
print(">>listening mode")


def mainExecution():

    Speak("Hello Boss..!") 
    Speak("i'm zaya, i'm ready to assist you...")

    while True:

        data = MicExecution()  
        Data = str(data)
        Replay = replaybrain(Data)
        Speak(Replay)

def clapdetect():
    query = Tester()
    if True:
        Speak("")      
        Speak(">>> Clap Detected..! >>>")
        Speak("")      
        mainExecution()
    else:
        pass


clapdetect()



