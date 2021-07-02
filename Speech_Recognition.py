import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source :
    r.adjust_for_ambient_noise(source,duration=5) #Adjust background noise
    print('.. Speak Now ..')

    audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        print('Recognized : ',text)
    except Exception as e:
        print('Couldn\'t recognize audio !')

