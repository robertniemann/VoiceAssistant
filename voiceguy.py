import speech_recognition as sr
import os
import pyttsx3

r = sr.Recognizer()
mic = sr.Microphone()
obj = pyttsx3.init()

def listenToText(r, mic):
    with sr.Microphone() as source:
        audio = r.listen(source)
    try:
        txt = r.recognize_google(audio)
    except sr.UnknownValueError:
        return ''
    else:
        return txt

def tts(obj, txt):
    obj.say(txt)
    obj.runAndWait()

#types of questions:
#1: search
#2: play music
#3: weather
#4: quit
#5: call
#6: text
#7: open app
#8: take photo

def callFunction(questionQuery):
    parts = questionQuery.split('call ')
    if len(parts) > 2:
        tts(obj, "I'm sorry, who were you trying to call?")
        txt = listenToText(r, mic)
        parts = ['',txt]
    elif len(parts) == 1:
        tts(obj, ("Calling " + parts[0]))
    else:
        tts(obj, ("Calling " + parts[1]))
    return True
        
def textFunction(questionQuery):
    parts = questionQuery.split('text ')
    if len(parts) > 2:
        tts(obj, "I'm sorry, who were you trying to text?")
        txt = listenToText(r, mic)
        parts = ['',txt]
    elif len(parts) == 1:
        tts(obj, 'What should I text ' + parts[0] + '?')
        txt = listenToText(r,mic)
        tts(obj, ("Texting " + parts[0] + ' ' + txt))
    else:
        tts(obj, 'What should I text ' + parts[0] + '?')
        txt = listenToText(r,mic)
        tts(obj, ("Texting " + parts[1] + ' ' + txt))
    return True
        
def quitFunction():
    tts(obj, ("Have a nice day"))
    return False

def absentQuitFunction():
    tts(obj, ("Did you need anything else?"))
    questionQuery = listenToText(r, mic)
    if (questionQuery == '') or (questionQuery == 'No'):
        tts(obj,'Goodbye')
        return False
    else:
        return True
    
def playFunction(questionQuery):
    parts = questionQuery.split('text ')
    if len(parts) > 2:
        tts(obj, "I'm sorry, what were you trying to play?")
        txt = listenToText(r, mic)
        parts = ['',txt]
    elif len(parts) == 1:
        tts(obj, ("Playing " + parts[0]))
    else:
        tts(obj, ("Playing " + parts[1]))
    return True

def photoFunction():
    tts(obj, "Opening Camera")
    return True

def weatherFunction(questionQuery):
    parts = questionQuery.split('in')
    tts(obj, "The weather in " + parts[-1] + ' is nice!')
    return True

def searchFunction(questionQuery):
    tts(obj, "Searching for " + questionQuery)
    return True

def listenAndApply(questionQuery):
    print(questionQuery)
    if 'call' in questionQuery:
        return callFunction(questionQuery)
    elif 'text' in questionQuery:
        return textFunction(questionQuery)
    elif 'open' in questionQuery:
        return openFunction(questionQuery)
    elif ('play' in questionQuery) or ('music' in questionQuery):
        return playFunction(questionQuery)
    elif ('take' in questionQuery) or ('picture' in questionQuery) or ('photo' in questionQuery):
        return photoFunction(questionQuery)
    elif ('weather' in questionQuery) or ('outside' in questionQuery):
        return weatherFunction(questionQuery)
    elif ('thank you' in questionQuery) or ('okay' in questionQuery) or ('stop' in questionQuery):
        return quitFunction()
    elif ('' == questionQuery):
        return absentQuitFunction()
    else:
        searchFunction(questionQuery)

def main():
    boolin = True
    tts(obj, "Hello")
    while(boolin):
        tts(obj, "How can I be of service")
        questionQuery = listenToText(r, mic)
        boolin = listenAndApply(questionQuery)
        
if __name__ == '__main__':
    main()