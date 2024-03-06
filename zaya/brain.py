#API key

fileopen = open("data\\api.txt","r")
API = fileopen.read()
fileopen.close()
print(API)


#Importing

import openai
from dotenv import load_dotenv
openai.api_key = API

#GPT-3

openai.api_key = API
load_dotenv
completion = openai.Completion

def replaybrain(question,chat_log = None):
    
        FileLog = open("database\\chat_log.txt","r")
        chat_log_template = FileLog.read()
        FileLog.close()
        if chat_log == None:
            chat_log = chat_log_template
    
    
        prompt = f'{chat_log}You : {question}\n zaya :'    
        response = completion.create(
            model="text-davinci-002",
            prompt=prompt,
            temperature=0.5,
            max_tokens=60,
            top_p=0.3,
            frequency_penalty=0.5,
            presence_penalty=0.5,
            stop=["\n", " zaya :"]
        )
        answer = response.choices[0].text.strip()
        chat_log_template_update = chat_log_template + f'You : {question}\n zaya : {answer}\n'
        FileLog = open("database\\chat_log.txt","w")
        FileLog.write(chat_log_template_update)
        FileLog.close()
        return answer

