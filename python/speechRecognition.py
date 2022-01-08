import speech_recognition as sr
import sys 
r = sr.Recognizer()

def getSTT(wavFile = '..\data\korean.wav'):
    korean_audio = sr.AudioFile(wavFile)
    with korean_audio as source:
        audio = r.record(source)
    text = r.recognize_google(audio_data=audio, language='ko-KR')
    print(text)

if __name__ == '__main__':
    getSTT(sys.argv[1]) if len(sys.argv) >= 2 else getSTT()
