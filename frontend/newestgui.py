from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, END
import ollama
from RealtimeSTT import AudioToTextRecorder
from multiprocessing import Process, Pipe
import multiprocessing as mp
from ollamaModel import ollamaModel
from speechtotext import start_speech_to_text
from texttospeech import startTextToSpeech
from PIL import Image, ImageTk

class MainW(Tk):
    def __init__(self, parent):
        Tk.__init__(self, parent)
        self.parent = parent
        self.geometry("890x600")
        self.configure(bg = "#FFFFFF")    
        self.resizable(False, False)
        
        # Initialize pipes and processes
        self.pipe_to_recorder, reciever = Pipe()
        self.pipe_to_ollama, ollama_reciever = Pipe()
        self.pipe_to_speech, reciever_speech = Pipe()
        
        # Create and start processes
        self.client_process = Process(target=ollamaModel, args=(ollama_reciever,))
        self.recorder_process = Process(target=start_speech_to_text, args=(reciever,))
        self.speech_process = Process(target=startTextToSpeech, args=(reciever_speech,))
        
        self.recorder_process.start()
        self.client_process.start()
        self.speech_process.start()
        
        # Initialize state variables
        self.recording = False
        self.waiting_for_speech = False
        self.waiting_for_ollama = False
        
        # Create UI elements
        self.mainWidgets()
        
        # Start periodic pipe checking
        self.check_pipes()

    def relative_to_assets(self, path: str) -> Path:
        OUTPUT_PATH = Path(__file__).parent
        ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\aisha\rubberDuckyV2\frontend\assets")
        return ASSETS_PATH / Path(path)
    
    def check_pipes(self):
        """Periodically check pipes for messages without blocking the UI"""
        # Update duck image based on state
        if self.waiting_for_ollama:
            self.canvas.itemconfig(self.duck_canvas_img, image=self.button_image_2)  # Thinking duck
        else:
            self.canvas.itemconfig(self.duck_canvas_img, image=self.button_image_1)  # Normal duck
        
        # Check for speech recognition results
        if self.waiting_for_speech and self.pipe_to_recorder.poll():
            self.waiting_for_speech = False
            message = self.pipe_to_recorder.recv()
            self.recording = False
            
            # Got speech, now send to Ollama
            self.entry_1.delete("1.0", END)
            self.entry_1.insert(END, "Ducky is thinking...")
            prompt = "Study guide: " + str(self.entry_2.get("1.0", END)) + " Student: " + message
            self.pipe_to_ollama.send(prompt)
            self.waiting_for_ollama = True
        
        # Check for Ollama response
        if self.waiting_for_ollama and self.pipe_to_ollama.poll():
            response = self.pipe_to_ollama.recv()
            self.entry_1.delete("1.0", END)
            self.entry_1.insert(END, response)
            self.pipe_to_speech.send(response)
            self.waiting_for_ollama = False
        
        # Schedule next check
        self.after(100, self.check_pipes)

    def recorder_button_click(self, event=None):
        """Handle button click to start/stop recording"""
        if self.waiting_for_ollama:
            return  # Don't allow new recording while processing
            
        if not self.recording:
            # Start recording
            self.pipe_to_recorder.send(True)
            self.recording = True
            self.waiting_for_speech = True
            self.entry_1.delete("1.0", END)
            self.entry_1.insert(END, "Listening...")
        else:
            # Stop recording and wait for result
            self.pipe_to_recorder.send(False)
            self.waiting_for_speech = True
            self.entry_1.delete("1.0", END)
            self.entry_1.insert(END, "Processing your speech...")

    def mainWidgets(self):
        # Create main canvas
        self.canvas = Canvas(
            self,
            bg = "#FFFFFF",
            height = 600,
            width = 890,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )
        self.canvas.place(x=0, y=0)
        
        # Background image
        self.image_image_1 = PhotoImage(file=self.relative_to_assets("image_1.png"))
        image_1 = self.canvas.create_image(445.0, 445.0, image=self.image_image_1)

        # Right text entry (Duck feedback)
        self.entry_image_1 = PhotoImage(file=self.relative_to_assets("entry_1.png"))
        entry_bg_1 = self.canvas.create_image(735.0, 350.5, image=self.entry_image_1)
        self.entry_1 = Text(
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_1.place(x=619.0, y=178.0, width=232.0, height=343.0)

        # Left text entry (Study material)
        self.entry_image_2 = PhotoImage(file=self.relative_to_assets("entry_2.png"))
        entry_bg_2 = self.canvas.create_image(153.0, 350.5, image=self.entry_image_2)
        self.entry_2 = Text(
            bd=0,
            bg="#000000",
            fg="#FFFFFF",
            highlightthickness=0
        )
        self.entry_2.place(x=37.0, y=178.0, width=232.0, height=343.0)

        # Header text
        self.canvas.create_text(
            271.0, 15.0,
            anchor="nw",
            text="Study Ducky",
            fill="#FFFFFF",
            font=("LondrinaSketch Regular", 70 * -1)
        )

        # Other labels
        self.canvas.create_text(
            46.0, 193.0,
            anchor="nw",
            text="You Said....",
            fill="#000000",
            font=("Inter", 12 * -1)
        )

        # Rectangles for section headers
        self.canvas.create_rectangle(24.0, 113.0, 337.0, 162.0, fill="#000000", outline="")
        self.canvas.create_rectangle(545.0, 113.0, 858.0, 162.0, fill="#D9D9D9", outline="")

        # Section header text
        self.canvas.create_text(
            573.0, 113.0,
            anchor="nw",
            text=" FeedDuck",
            fill="#000000",
            font=("Lohit Devanagari", 30 * -1)
        )
        self.canvas.create_text(
            47.0, 113.0,
            anchor="nw",
            text="Studucky Material",
            fill="#FFFFFF",
            font=("Lohit Devanagari", 30 * -1)
        )

        # Load duck images
        button_path = self.relative_to_assets("button_1.png")
        pil_button = Image.open(button_path)
        self.button_image_1 = ImageTk.PhotoImage(pil_button)
        
        button_path = self.relative_to_assets("button_2.png")
        pil_button = Image.open(button_path)
        self.button_image_2 = ImageTk.PhotoImage(pil_button)
        
        # Get image dimensions for positioning
        width, height = self.button_image_1.width(), self.button_image_1.height()
        
        # Create clickable duck image
        self.duck_canvas_img = self.canvas.create_image(
            314.0 + width / 2,
            193.0 + height / 2,
            image=self.button_image_1,
            anchor="center"
        )
        
        # Bind click event to the duck image
        self.canvas.tag_bind(self.duck_canvas_img, "<Button-1>", self.recorder_button_click)

if __name__ == "__main__":
    gui = MainW(None)
    gui.mainloop()