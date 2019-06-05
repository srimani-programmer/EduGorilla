from gtts import gTTS

fhandle = open('sample.txt','r')

fhandle = fhandle.read()

tts = gTTS(text=fhandle, lang='en')
tts.save('file.mp3')