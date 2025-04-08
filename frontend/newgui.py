from pathlib import Path

from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, END
import ollama
from RealtimeSTT import AudioToTextRecorder
from multiprocessing import Process, Pipe
import multiprocessing as mp
from speechtotext import start_speech_to_text

class MainW(Tk):
    def __init__(self, parent):
        Tk.__init__(self, parent)
        self.parent = parent
        self.mainWidgets()
        self.geometry("890x600")
        self.configure(bg = "#FFFFFF")    
        self.resizable(False, False)
        self.pipe_to_recorder, reciever = Pipe()
        self.client = ollama.Client("localhost:11434")
        self.recorder_process = Process(target=start_speech_to_text, args=(reciever,))
        self.recorder_process.start()
        self.recording = False


    def relative_to_assets(self, path: str) -> Path:
        OUTPUT_PATH = Path(__file__).parent
        ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\aisha\rubberDuckyV2\frontend\assets")
        return ASSETS_PATH / Path(path)

    def mainWidgets(self):
        def recorder_button():
            if self.recording == False:
                self.pipe_to_recorder.send(True)
                self.recording = True
            else:
                self.pipe_to_recorder.send(False)
                while not self.pipe_to_recorder.poll():
                    pass
                message = self.pipe_to_recorder.recv()
                print("RECIEVED", message)
                self.entry_1.delete("1.0",END)
                self.entry_1.insert(END, "Ducky is thinking...")
                response = self.client.generate(model="rubberduck", prompt="Study guide: " + str(self.entry_2.get("1.0", END)) + " Student: " + message)
                self.entry_1.delete("1.0",END)
                self.entry_1.insert(END, response.response)
        canvas = Canvas(
            self,
            bg = "#FFFFFF",
            height = 600,
            width = 890,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        canvas.place(x = 0, y = 0)
        self.image_image_1 = PhotoImage(
            file=self.relative_to_assets("image_1.png"))
        image_1 = canvas.create_image(
            445.0,
            445.0,
            image=self.image_image_1
        )

        self.entry_image_1 = PhotoImage(
            file=self.relative_to_assets("entry_1.png"))
        entry_bg_1 = canvas.create_image(
            735.0,
            350.5,
            image=self.entry_image_1
        )
        self.entry_1 = Text(
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_1.place(
            x=619.0,
            y=178.0,
            width=232.0,
            height=343.0
        )

        self.entry_image_2 = PhotoImage(
            file=self.relative_to_assets("entry_2.png"))
        entry_bg_2 = canvas.create_image(
            153.0,
            350.5,
            image=self.entry_image_2
        )
        self.entry_2 = Text(
            bd=0,
            bg="#000000",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_2.place(
            x=37.0,
            y=178.0,
            width=232.0,
            height=343.0
        )

        canvas.create_text(
            271.0,
            15.0,
            anchor="nw",
            text="Study Ducky",
            fill="#FFFFFF",
            font=("LondrinaSketch Regular", 70 * -1)
        )

        canvas.create_text(
            46.0,
            193.0,
            anchor="nw",
            text="You Said....",
            fill="#000000",
            font=("Inter", 12 * -1)
        )

        canvas.create_rectangle(
            24.0,
            113.0,
            337.0,
            162.0,
            fill="#000000",
            outline="")

        canvas.create_rectangle(
            545.0,
            113.0,
            858.0,
            162.0,
            fill="#D9D9D9",
            outline="")

        canvas.create_text(
            573.0,
            113.0,
            anchor="nw",
            text=" FeedDuck",
            fill="#000000",
            font=("Lohit Devanagari", 30 * -1)
        )

        canvas.create_text(
            47.0,
            113.0,
            anchor="nw",
            text="Studucky Material",
            fill="#FFFFFF",
            font=("Lohit Devanagari", 30 * -1)
        )

        self.button_image_1 = PhotoImage(
            file=self.relative_to_assets("button_1.png"))
        button_1 = Button(
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=recorder_button,
            relief="flat"
        )
        button_1.place(
            x=314.0,
            y=193.0,
            width=281.0,
            height=305.0
        )

if __name__ == "__main__":
    gui = MainW(None)
    
    gui.mainloop()