import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib



engine=pyttsx3.init('sapi5')
voices =engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(audio):
	engine.say(audio)
	engine.runAndWait()
def wishme():
	hour=int(datetime.datetime.now().hour)
	if hour>=0 and hour<12:
		speak("Good morning kumar")
	elif hour>=12 and hour<18:
		speak("Good afternoon  kumar")
	else:
		speak("Good evening kumar")
	speak("I am your friend jarvis how can i help you")
def takecmd():
	r=sr.Recognizer()
	with sr.Microphone() as source:
		print("Listening...")
		r.pause_threshold=1
		audio=r.listen(source)
	try:
		print("recognising")
		query=r.recognize_google(audio,language='en-in')
		print(f"user said: {query}\n")
	except Exception as e:
		print(e)
		print("say that again")
		return "None"
	return query
def sendEmail(to,content):
	server=smtplib.SMTP('smtp.gmail.com',587)
	server.ehlo()
	server.starttls()
	server.login("490 kumar",'password')
	server.sendmail('20a21a0490ksk@gmail.com',to,content)
	server.close()




if __name__ == "__main__":
	wishme()
	k=1
	while(k):
		query=takecmd().lower()
		if('about' in query):
			speak("Searching wikipedia")
			query=query.replace("about",'')
			results=wikipedia.summary(query,sentences=2)
			speak("according to wikipedia")
			print(results)
			speak(results)
		elif('youtube' in query):
			webbrowser.open("youtube.com")
		elif('google' in query):
			webbrowser.open("google.com")
		elif('vs code' in query):
			webbrowser.open('"C:\\Users\\ksk\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"')
		elif('send email' in query):
			try:
				speak("what should i say")
				content=takecmd()
				to="kksatyanarayana944@gmail.com"
				sendEmail(to,content)
				speak("email has been sent")
			except Exception as e:
				print(e)
				speak("sry i am not able to send the email")
		elif(('shutdown'or 'shut down') in query):
			speak(" ok i am shutting down have a nice day")
			k=0
		else:
			speak("i dont no")

