import speech_recognition as sr

class getText:
    def __init__(self,filename):
        self.filename
        self.getText()
        
    
    def getText(self):
        r = sr.Recognizer()
        # open the file
        with sr.AudioFile(filename) as source:
            # listen for the data (load audio to memory)
            audio_data = r.record(source)
            # recognize (convert from speech to text)
            text = r.recognize_google(audio_data)
            print(text)

