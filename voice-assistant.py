import webbrowser
import speech_recognition as sr
burl = "https://www.youtube.com/results?search_query="

def main():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Please say something...")
        audio=r.listen(source)
        try:
            s=r.recognize_google(audio)
            print(s)
            webbrowser.open(burl+s)
        except Exception as e:
            print("Error : "+str(e))
main()