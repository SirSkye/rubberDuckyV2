from pathlib import Path

from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import ollama
from RealtimeSTT import AudioToTextRecorder

class MainW(Tk):
    def __init__(self, parent):
        Tk.__init__(self, parent)
        self.parent = parent
        self.mainWidgets()
        self.geometry("890x600")
        self.configure(bg = "#FFFFFF")    
        self.resizable(False, False)
        # self.recorder = AudioToTextRecorder()
        # self.client = ollama.Client()

    def relative_to_assets(self, path: str) -> Path:
        OUTPUT_PATH = Path(__file__).parent
        ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\aisha\Tkinter-Designer\rachelsDesign\build\assets\frame0")
        return ASSETS_PATH / Path(path)

    def mainWidgets(self):
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
        canvas.create_rectangle(
            451.0,
            178.0,
            863.0,
            569.0,
            fill="#D9D9D9",
            outline="")

        canvas.create_rectangle(
            25.0,
            178.0,
            437.0,
            569.0,
            fill="#000000",
            outline="")

        canvas.create_rectangle(
            37.0,
            16.0,
            853.0,
            95.0,
            fill="#000000",
            outline="")

        canvas.create_text(
            375.0,
            0.0,
            anchor="nw",
            text="Duck",
            fill="#FFFFFF",
            font=("Lohit Devanagari", 60 * -1)
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
            33.0,
            113.0,
            346.0,
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
            text="Duck Feedback",
            fill="#000000",
            font=("Lohit Devanagari", 30 * -1)
        )

        canvas.create_text(
            47.0,
            113.0,
            anchor="nw",
            text="Study Material",
            fill="#FFFFFF",
            font=("Lohit Devanagari", 30 * -1)
        )

        self.button_image_1 = PhotoImage(
            file=self.relative_to_assets("button_1.png"))
        button_1 = Button(
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_1 clicked"),
            relief="flat"
        )
        button_1.place(
            x=360.0,
            y=110.0,
            width=59.0,
            height=59.0
        )
        button_1.lift()

gui = MainW(None)
print("MAINLOPPP")
gui.mainloop()