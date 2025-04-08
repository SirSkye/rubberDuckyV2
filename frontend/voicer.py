# import pyttsx3
# engine = pyttsx3.init()
# voices = engine.getProperty('voices')
# engine.setProperty("voice", voices[1].id)
# engine.say("I will speak this text")
# engine.runAndWait()

from RealtimeTTS import TextToAudioStream, SystemEngine, GTTSEngine

engine = GTTSEngine() # replace with your TTS engine
voices = engine.get_voices()
print(voices)
stream = TextToAudioStream(engine)
print("DONE")
stream.feed("Hello world! How are you today?")
stream.play_async()