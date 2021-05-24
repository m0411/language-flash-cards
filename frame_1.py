from tkinter import *
import random
from frame_2 import FrameTwo


class FrameOne:

    def __init__(self, frame, color1, color2, frame2, color3):
        self.text = Label(frame, text="Flash cards:", font=("Arial", 50, "bold"), fg=color1, bg=color2)
        self.text.grid(row=0, column=0, columnspan=6, sticky="EW")
        self.text.config(padx=210, pady=50)
        self.text2 = Label(frame, text="pick a language", font=("Arial", 30, "italic"), fg=color1, bg=color2)
        self.text2.grid(row=1, column=0, columnspan=6, sticky="EW")
        self.text2.config(pady=30)
        self.text3 = Label(frame, text="The button below will pick a random language from the languages above.",
                           font=("Arial", 10, "normal"), fg=color1, bg=color2)
        self.text3.grid(row=5, column=1, columnspan=4, sticky="EW")
        self.text3.config(pady=50)
        self.bg_color = color3
        with open("data.csv", encoding="utf8") as file:
            data = file.readlines()
            del data[0]
            self.dict_info = {
                "English": [item.split(",")[0] for item in data],
                "German": [item.split(",")[1] for item in data],
                "Turkish": [item.split(",")[2] for item in data],
                "Spanish": [item.split(",")[3] for item in data],
                "French": [item.split(",")[4] for item in data],
                "Arabic": [item.split(",")[5] for item in data],
                "Japanese": [item.split(",")[6] for item in data],
            }
        self.buttons(frame, frame2)

    def chosen_language(self, language, frame):
        frame_2 = FrameTwo(language, frame)
        frame.tkraise()
        frame_2.canvas.config(highlightthickness=0)
        frame_2.canvas.create_text(380, 263, text=random.choice(self.dict_info["English"]), font=("Ariel", 60, "bold"))
        frame_2.canvas.grid(row=1, column=0, columnspan=2)

    def buttons(self, frame, frame2):
        german = Button(frame, text="German", font=("Arial", 15, "normal"),
                        command=lambda: self.chosen_language("German", frame2))
        german.grid(row=2, column=1, sticky="W")
        turkish = Button(frame, text="Turkish", font=("Arial", 15, "normal"),
                         command=lambda: self.chosen_language("Turkish", frame2))
        turkish.grid(row=3, column=1, sticky="W")
        spanish = Button(frame, text="Spanish", font=("Arial", 15, "normal"),
                         command=lambda: self.chosen_language("Spanish", frame2))
        spanish.grid(row=4, column=1, sticky="W")
        french = Button(frame, text="French", font=("Arial", 15, "normal"),
                        command=lambda: self.chosen_language("French", frame2))
        french.grid(row=2, column=4, sticky="E")
        arabic = Button(frame, text="Arabic", font=("Arial", 15, "normal"),
                        command=lambda: self.chosen_language("Arabic", frame2))
        arabic.grid(row=3, column=4, sticky="E")
        japanese = Button(frame, text="Japanese", font=("Arial", 15, "normal"),
                          command=lambda: self.chosen_language("Japanese", frame2))
        japanese.grid(row=4, column=4, sticky="E")
        random_button = Button(frame, text="Random", font=("Arial", 15, "normal"),
                               command=lambda: self.chosen_language(random.choice(["German",
                                                                                   "Turkish", "Spanish",
                                                                                   "French", "Arabic", "Japanese"]),
                                                                    frame2))
        random_button.grid(row=6, column=2, columnspan=2, sticky="EW")
        home = Button(frame2, text="Home", font=("Arial", 15, "normal"), command=lambda: frame.tkraise())
        home.grid(row=0, column=0, sticky="W")
        home.config(padx=20)
