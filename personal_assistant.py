import datetime
import pyaudio
import pyttsx3
import webbrowser as wb
import speech_recognition as sr
import wikipedia 
import smtplib
import psutil
import pyjokes
import os
import pyautogui
import random
import wolframalpha
import json
import requests
from urllib.request import urlopen
import time

WOLFRAM_APP_ID = 'your wolframalpha app ID'
NEWS_API = 'your news api key'

Time=datetime.datetime.now().strftime("%I:%M:%S")

def speak(Text):
    engine=pyttsx3.init()
    voices=engine.getProperty('voices')
    print(voices[0])
    engine.setProperty('voice', voices[1].id)
    engine.say(Text)
    engine.runAndWait()
    
def time_():
    Time=datetime.datetime.now().strftime("%I:%M:%S")#for 12 hours clock
    speak('The current time is')
    speak(Time)

def date_():
    year=datetime.datetime.now().year
    month=datetime.datetime.now().month
    day=datetime.datetime.now().day
    speak('The current date is')
    speak(day)
    speak(month)
    speak(year)
    speak(("%I:%M:%S"))
    print(("%I:%M:%S"))
    
def wishme():
    speak('welcome sir!')
    time_()
    date_()
    
    
    #Greetings
    hour=datetime.datetime.now().hour
    if hour>=6 and hour<=12:
        speak('Good morning sir!')
        
    elif hour>=12and hour<=18:
        speak('Good afternoon sir!')
        
    elif hour>=18 and hour<24:
        speak('Good evening sir!')
        
    else :
        speak('Good night sir!')
    
    speak('Julia at your service, please tell me how can I help you today sir?')


def TakeCommand():
    r =sr.Recognizer()
    with sr.Microphone() as source:
        print('listening...')
        speak('listening..')
        #r.pause_threshold=1
        audio=r.record(source,duration=5)
    
    try:
      print('Recognizing....')
      query=r.recognize_google(audio,language='en-US')
      print(query)

    except Exception as e:
        print(e)
        print('say that again please...')
        return 'None'

    return query


def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('senderemail@gmail.com','1234')
    server.sendmail('senderemail@gmail.com',to,content)
    server.close()
    
def cpu():
    usage=str(psutil.cpu_percent())
    speak('CPU is at'+usage)
    battery=psutil.sensors_battery()
    speak('your battery is at '+str(battery.percent)+' percent')
    
    
def joke():
    speak(pyjokes.get_joke())
    
def screenshot():
    img=pyautogui.screenshot()
    img.save(f'screenshot_{datetime.datetime.now()}.png')
    speak('Screenshot taken sir!')


def wolfram():
    wolframalpha_app_id='EVU44W-55R4L6P66Q'
    client=wolframalpha.Client(wolframalpha_app_id)
    res=client.query(query)

    try:
        print(next(res.results).text)
        speak(next(res.results).text)
            
            
    except StopIteration:
        print('sorry no results!')
        
if __name__ == "__main__":
    clear_console=lambda :os.system('cls')
    clear_console()
    
    while True:
        query=TakeCommand().lower()
        print(query)
        
        if 'time' in query:
            time_()
            
        elif 'date' in query:
            date_()
            
                    
            
        elif 'send email' in query:
            try:
                
                speak('what should I say?')
                content=TakeCommand()
                
                speak('who is the receiver please?')
                receiver=input("please enter receiver's email address")
                sendEmail(receiver,content)
                speak('Email has been sent successfully')
                
            except Exception as e:
                print (e)
                speak('sorry unable to send email')
                
        elif 'chrome' in query:
            speak('please what should I search?')
            chromepath= 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            search=TakeCommand().lower()
            wb.get(chromepath).open_new_tab(search+'.com')
            
            
        elif 'youtube' in query:
            speak('what should I search?')
            search_terms=TakeCommand().lower()
            wb.open('https://www.youtube.com/results?search_query='+search_terms)
            
            
        elif 'google' in query:
            speak('please what should I search?')
            search_term=TakeCommand().lower()
            speak('searching...')
            wb.open('https://www.google.com/search?q='+search_term)
            
            
        elif  'wikipedia' in query:
           speak('what should I search on wikipedia?')
           query=TakeCommand().lower()
           speak('searching...')
           query=query.replace('wikipedia','')
           result=wikipedia.summary(query,sentences=3)
           speak('According to wikipedia')
           print(result)
           speak(result)
           
        elif 'cpu' in query:
            cpu()
            
        elif 'joke'in query:
            joke()
           
        elif 'go offline' in query:
            speak('Going offline boss!')
            quit()
            
        elif 'excel' in query:
            speak('opening microsof excel...')
            #ms_word=r'E:Office/office16/WINWORD.EXE' 
            ms_excel=r'C:\Program Files (x86)\Microsoft Office\Office14\EXCEL.EXE'            
            os.startfile(ms_excel)
        
        elif 'write a note' in query:
            speak('what should I write boss?')
            notes=TakeCommand()
            file=open('notes.txt','w')
            speak('Sir should I include the date and time?')
            answer=TakeCommand()
            if 'yes' in answer or 'sure' in answer:
                strTime=datetime.datetime.now().strftime('%H:%M:%S')
                file.write(strTime)
                file.write(':-')
                file.write(notes)
                speak('Done taking notes sir!')
                
            else:
                file.write(notes)
                
        elif 'show note' in query:
            file=open('notes.txt','r')
            print(file.read())
            speak(file.read())
            
        elif 'screenshot' in query:
            screenshot()
            
        elif 'play'  in query:
            audio_dir='C:/Users/user/Desktop/Audio'
            dir_s=os.listdir(audio_dir)
            print(dir_s)
            speak('what no should I play?')
            ans=TakeCommand().lower()
            while 'number' not in ans and ans!= 'random':
                speak('I could not understand to,please try again!')
                ans=TakeCommand().lower()
            if 'number' in ans:
                no=int(ans.replace('number',''))
            elif 'random' or 'you choose' in ans:
                no=random.randint(1,100)
            
            
           try:
             os.startfile(os.path.join(audio_dir,dir_s[no]))
           except Exception as e:
             print(str(e))
             
            
            
        elif  'remember that' in query:
            speak('what should I remember')
            memory=TakeCommand()
            speak('you asked me to remember that'+memory)
            remember=open('memory.txt','w')
            remember.write(memory)
            remember.close()
            
        elif 'do you remember anything' in query:
            remember=open('memory.txt','r')
            speak('you asked me to remember that'+remember.read())
             
                
                
            
        elif 'wikipedia'  in query:
           speak('searching..')
           query=query.replace('wikipedia','')
           result=wikipedia.summary(query,sentence=3)
           speak('According to wikipedia..')
           print(result)
           speak(result)
           
        elif 'news' in query:
            try:
               jsonObj=urlopen(NEWS_API)
               data =json.load(jsonObj)
               i=1
            
               speak('Here are some top headlines for entertainment industry')
               print('-------------------TOP HEADLINES------------------')
               for item in data['articles']:
                   
                    print(str(i)+'.'+item['title']+'\n')
                    print(item['description']+'\n')
                    speak(item['title'])
                    i+=1
                    
            except Exception as e:
                      print(str(e))
                      
        elif 'stop listening' in query:
               speak('For how many seconds should I stop listening boss?')
               ans=int(TakeCommand())
               time.sleep(ans)
               print(str(ans)+'seconds')
            
            
            
        elif 'where is' in query:
            query=query.replace('where is','')
            location=query
            speak('User asked to locate'+location)
            wb.open_new_tab('https://www.google.com/maps/place/'+location)
            
            
        elif 'calculate' in query:
            client=wolframalpha.Client(WOLFRAM_APP_ID)
            indx=query.lower().split().index('calculate')
            query=query.split()[indx+1:]
            res=client.query(''.join(query))
            answer=next(res.results).text 
            print('The answer is: ',answer)         
            speak('The answer is: '+answer)        



        elif 'what is' or 'who is' in query:
            wolfram()

            
        elif 'listen' in query:
            speak('Yes boss I am listening!')
            

        elif 'log out' in query:
            os.system('shutdown -1')
            
        elif 'restart' in query:
            os.system('shutdown /r /t 1')
                
        elif 'shut down'  or 'shutdown'in query:
            speak('shutting down sir!')
            
            os.system('shutdown /s /t 1')
            
        

    
    
