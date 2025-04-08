from RealtimeSTT import AudioToTextRecorder
from multiprocessing import Pipe

class SpeechToText():
    def __init__(self, pipe_conn):
        self.recorder = AudioToTextRecorder()
        self.can_record = False
        self.pipe:bool = pipe_conn
        self.pipeSend:str = pipe_conn

    
    def main(self):
        while True:
            message = self.pipe.recv()
            if(message == True):
                if(self.can_record):
                    self.can_record = False
                    self.recorder.start()
            if(message == False):
                    self.recorder.stop()
                    self.pipeSend.send(self.recorder.text())
                    self.can_record = True


