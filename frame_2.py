from tkinter import *
from PIL import Image, ImageTk


class FrameTwo:

    def __init__(self, language, frame):
        self.canvas = Canvas(master=frame, width=800, height=526)

        self.card_front = PhotoImage(master=frame, file="Images/card_front.png")
        self.card_back = PhotoImage(master=frame, file="Images/card_back.png")

        self.canvas.create_image(380, 263, image=self.card_front)
        self.canvas.create_text(380, 150, text=f"English to {language}", font=("Ariel", 40, "italic"))

        self.cross_image = PhotoImage(master=frame, file="Images/wrong_mark.png")
        self.wrong_button = Button(frame, image=self.cross_image)
        self.wrong_button.grid(row=2, column=0)

        self.tick_image = PhotoImage(master=frame, file="Images/tick_mark.png")
        self.correct_button = Button(frame, image=self.tick_image)
        self.correct_button.grid(row=2, column=1)

