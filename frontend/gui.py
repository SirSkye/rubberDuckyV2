from pathlib import Path

from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import ollama

client = ollama.Client()

class MainW(Tk):
    def __init__(self, parent):
        Tk.__init__(self, parent)
        self.parent = parent
        self.mainWidgets()
        self.geometry("816x529")
        self.configure(bg = "#FFFFFF")    
        self.resizable(False, False)

    def relative_to_assets(self, path: str) -> Path:
        OUTPUT_PATH = Path(__file__).parent
        ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\aisha\Tkinter-Designer\output\build\assets\frame0")
        return ASSETS_PATH / Path(path)

    def mainWidgets(self):
        canvas = Canvas(
            self,
            bg = "#FFFFFF",
            height = 529,
            width = 816,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge")
        canvas.place(x = 0, y = 0)
        entry_image_1 = PhotoImage(
            file=self.relative_to_assets("entry_1.png"))
        entry_bg_1 = canvas.create_image(
            578.0,
            160.5,
            image=entry_image_1
        )
        entry_1 = Text(
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0
        )
        entry_1.place(
            x=374.0,
            y=47.0,
            width=408.0,
            height=225.0
        )

        canvas.create_rectangle(
            14.0,
            265.0,
            374.0,
            512.0,
            fill="#D9D9D9",
            outline="")

        canvas.create_rectangle(
            365.0,
            8.0,
            791.0,
            38.0,
            fill="#D9D9D9",
            outline="")

        canvas.create_text(
            541.0,
            16.0,
            anchor="nw",
            text="Study Material",
            fill="#000000",
            font=("Inter", 12 * -1)
        )

        canvas.create_text(
            156.0,
            250.0,
            anchor="nw",
            text="You Said....",
            fill="#000000",
            font=("Inter", 12 * -1)
        )

        button_image_1 = PhotoImage(
            file=self.relative_to_assets("button_1.png"))
        submitBtn = Button(
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_1 clicked"),
            relief="flat"
        )
        submitBtn.place(
            x=443.0,
            y=276.0,
            width=306.0,
            height=30.0
        )

        canvas.create_text(
            570.0,
            283.0,
            anchor="nw",
            text="Submit",
            fill="#000000",
            font=("Inter", 12 * -1)
        )

gui = MainW(None)

gui.mainloop()