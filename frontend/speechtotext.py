from RealtimeSTT import AudioToTextRecorder

class SpeechToText():
    def __init__(self, queue):
        self.recorder = AudioToTextRecorder()
        self.recording = False
        self.queue = queue
    
    def main(self):

