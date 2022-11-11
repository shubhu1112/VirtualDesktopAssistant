import wikipedia
import webbrowser
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import pyautogui
import speedtest
import sys
from utils import *

print("Initializing Virtual Desktop Assistant")
speak('')
wishMe()
takeCommand()


class allfuncs():

    def main(self):
        speak("Initializing Virtual desktop Assistant...")
        wishMe()
        query = takeCommand()
        if query == None:
            return False

        if 'wikipedia' in query.lower():
            speak('searching wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            print(results)
            speak(results)

        elif 'open youtube' in query.lower():
            speak("Please wait.. , Opening Youtube")
            url = "youtube.com"
            chrome_path = 'c:/program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open(url)

        elif 'open google' in query.lower():
            url = "google.com"
            speak("Please wait, Opening Google")
            chrome_path = 'c:/program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open(url)

        elif 'play music' in query.lower():
            speak("Please wait, Playing music")
            url = "https://youtu.be/pJAXt1D68IE"
            chrome_path = 'c:/program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            print("Playing Music.....")
            webbrowser.get(chrome_path).open(url)

        elif 'Whats time now' in query.lower():
            strTime = datetime.datetime.now().strftime("%H:%M:%S pycharm")
            speak(f" the time is {strTime}")

        elif 'send mail' in query.lower():
            speak("Please wait. Sending mail")
            sender = 'shubhu0899@gmail.com'
            reciever = 'akpathak59@gmail.com'

            msg = MIMEMultipart()
            msg['From'] = ''.format(sender)
            msg['To'] = ','.join(reciever)
            msg['Subject'] = "Hello, This mail is sent through python code"
            body = "Total no. of files : 9"
            msg.attach(MIMEText(body, 'plain'))
            filename = "output1_2022_09_08_10_24_49_PM.txt"
            attachment = open("C:/Users/ASUS/PycharmProjects/pythontutorial/output1_2022_09_08_10_24_49_PM.txt", "rb")

            p = MIMEBase('application', 'octet-stream')
            p.set_payload((attachment).read())
            encoders.encode_base64(p)

            p.add_header('Content-Disposition', "attachment; filename= %s" % filename)

            msg.attach(p)
            s = smtplib.SMTP('smtp.gmail.com', 587)
            s.starttls()
            s.login(sender, 'wukd nrxq cbht pavs')
            text = msg.as_string()
            s.sendmail(sender, reciever, text)
            s.quit()
            print('Mail Sent Successfully')
            speak("Mail sent successfully")

        elif 'google search' in query.lower():
            speak("What you want to search")
            r = sr.Recognizer()
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source)

                try:
                    text = r.recognize_google(audio)
                except:
                    print("Did not recognize")
            print("Loading Results... Please wait..")
            speak("Loading Results... Please Wait...")
            chrome_path = 'c:/program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path)
            webbrowser.open("https://www.google.com/search?q=" + text)

        elif 'open facebook' in query.lower():
            speak("please wait... opening facebook")
            url = "www.facebook.com"
            chrome_path = 'c:/program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open(url)

        elif 'open instagram' in query.lower():
            speak("please wait... Opening instagram...")
            url = ("www.instagram.com")
            chrome_path = 'c:/program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open(url)

        elif 'open' in query.lower():
            query = query.replace("open", "")
            query = query.replace("Jarvis", "")
            pyautogui.press("super")
            pyautogui.typewrite(query)
            pyautogui.sleep(2)
            pyautogui.press("enter")

        elif 'internet speed' in query.lower():
            st = speedtest.Speedtest()
            upload_net = st.upload() / 1048576
            download_net = st.download() / 1048576
            print("Wifi upload speed is", upload_net)
            print("Wifi download speed is", download_net)
            speak(f"Wifi download speed is {download_net}")
            speak(f"Wifi upload speed is {upload_net}")

        elif 'site' in query.lower():
            c = (query[4:].strip())
            d = c.replace(" ", "")
            d += '.com'
            print(d)
            speak(d)
            webbrowser.get('c:/program Files (x86)/Google/Chrome/Application/chrome.exe %s').open(d)
            sys.exit()
        elif 'What is your name' in query.lower():
            speak('My name is Friday.. I am Your assistant ')
        else:
            return False

    def looping(self):
        for attempts in range(0, 3):
            print("Attempts : " + str(attempts))
            res = self.main()
            if res != False:
                print("Query Executed")
                break


a = allfuncs()
a.looping()
