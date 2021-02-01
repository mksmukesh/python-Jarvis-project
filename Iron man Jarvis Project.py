import pyttsx3 #pip install pyttsx3
import datetime
import speech_recognition as sr #pip install SpeechRecognition
import wikipedia #pip install wikipedia
import smtplib
import webbrowser as wb
import os
import pyautogui #pip install pyautogui
import psutil #pip install psutil
import pyjokes #pip install pyjokes

engine= pyttsx3.init()

def speak(audio):
     engine.say(audio)
     engine.runAndWait()



def time():
    speak("Current time is")
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak(Time)
     
def date():
    year = int (datetime.datetime.now().year)
    month = int (datetime.datetime.now().month)  
    day = int (datetime.datetime.now().day)
    speak("current date is")
    speak(year)
    speak(month)
    speak(day)


def wishme():
    speak("Welcome back Mukesh sir!")
    
    time()
    
    date()
    hour= datetime.datetime.now().hour
    if hour>=6 and hour<12:
        speak("Good morning mukesh sir!")
    elif hour>=12  and hour<18:
        speak("Good afternoon mukesh sir!")
    elif hour>=18 and hour<24:
        speak("Good evening mukesh sir!")
    else:
        speak("Good night Mukesh sir!")          
    speak("This is Jarvis created by Mukesh ....Please tell me how can i help sir!")



def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
          print("Listening sir...")
          r.pause_threshold = 1
          audio = r.listen(source)

    try:
        print("Recognizing..")
        query = r.recognize_google(audio, language='en-in')
        print(query)     
    
    except Exception as e:
        print(e)
        speak("say that again please")
        return "none"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('abc@gmail.com','12345')
    server.sendmail('abc@gmail.com',to,content)
    server.close()

def screenshot():
    img = pyautogui.screenshot()
    img.save("C:\\Users\\KIIT\\Desktop\\DSA\\ss.png")

def cpu():
    usage = str(psutil.cpu_percent())
    speak("cpu is at"+usage)
    battery= psutil.sensors_battery()
    speak("battery is at ")
    speak(battery.percent)

def jokes():
    speak(pyjokes.get_joke())


if __name__=="__main__":
    wishme()
    while True:
        query=takecommand().lower()
        if 'time' in query:
            time()
        elif 'date' in query:
            date()
        elif 'wikipedia' in query:
            speak("Searching...")
            query = query.replace("wikipedia","")
            result=wikipedia.summary(query,sentences = 2)
            print(result)
            speak(result)    
        elif 'send email' in query:
            try:
                speak("what should i say?")
                content = takecommand()
                to = 'faltukam999@gmail.com'
                sendEmail(to,content)
                speak("email has been sent!")
            except Exception as e:
                print(e)
                speak("email has not been sent!")    
        elif 'search in chrome' in query:
            speak("what should i search?")
            chromepath = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            search =takecommand().lower()
            wb.get(chromepath).open_new_tab(search+'.com')

        elif 'logout' in query:
            os.system("shutdown -l")

        elif 'logout' in query:
            os.system("shutdown /s /t 1")

        elif 'logout' in query:
            os.system("shutdown /r /t 1")


        elif 'play songs' in query:
            songs_dir = 'E:\\Music'
            songs = os.listdir(songs_dir)
            os.startfile(os.path.join(songs_dir,songs[0]))

        elif 'remember that' in query:
            speak("What should i remember?")
            data=takecommand()
            speak("you said me to remember that" +data)
            remember= open('data.txt','w')
            remember.write(data)
            remember.close()    

        elif 'screenshot' in query:
            screenshot()
            speak("done!")

        elif 'cpu'in query:
            cpu()

        elif 'joke' in query:
            jokes()


        elif 'offline' in query:
           quit()



