from RealtimeSTT import AudioToTextRecorder

def start_speech_to_text(pipe):
    recorder = AudioToTextRecorder()
    can_record = False
    print("RAN")

    while True:
        if pipe.poll():
            print("Polling")
            message = pipe.recv()
            print(message)
            if message == True:
                recorder.start()
            if message == False:
                recorder.stop()
                recorded = recorder.text()
                print(recorded)
                pipe.send(recorded)