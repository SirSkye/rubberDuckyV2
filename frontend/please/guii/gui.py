
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\rache\YRHacks2025\rachel\rubberDuckyV2\frontend\please\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("890x600")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 600,
    width = 890,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    445.0,
    445.0,
    image=image_image_1
)

canvas.create_rectangle(
    451.0,
    178.0,
    863.0,
    569.0,
    fill="#D9D9D9",
    outline="")

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    231.0,
    373.5,
    image=entry_image_1
)
entry_1 = Text(
    bd=0,
    bg="#000000",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=37.0,
    y=178.0,
    width=388.0,
    height=389.0
)

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
    fill="#FFFFFF",
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

def start_reco():
    print("button clicked")

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))

button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=start_reco,
    relief="flat"
)
button_1.place(
    x=360.0,
    y=110.0,
    width=59.0,
    height=59.0
)

    
    
    
window.resizable(False, False)
window.mainloop()
