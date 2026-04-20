import speech_recognition as sr

def get_voice():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak now...")
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        return text.lower()
    except:
        return "error"