from tkinter import *
from tkinter import messagebox
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

# Paths
Card_Back = r"E:\Documents_Files\RobinData\PYTHON\RawDataofpng\CARD_BACK.png"
Card_Front = r"E:\Documents_Files\RobinData\PYTHON\RawDataofpng\CARD_FRONT.png"
Check = r"E:\Documents_Files\RobinData\PYTHON\RawDataofpng\CHECK.png"
Wrong = r"E:\Documents_Files\RobinData\PYTHON\RawDataofpng\WRONG.png"
csv_file_data = r"E:\Documents_Files\RobinData\PYTHON\RawDataofcsv\FRENCH_WORDS.csv"

# Load Data
Words_csv_Data = pandas.read_csv(csv_file_data)
Words_Data = Words_csv_Data.to_dict(orient="records")

current_card = {}
flip_timer = None
learned_count = 0

def flash_card():
    global current_card, flip_timer
    if len(Words_Data) == 0:
        return

    if flip_timer is not None:
        window.after_cancel(flip_timer)

    current_card = random.choice(Words_Data)

    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_image, image=FrontImage)

    flip_timer = window.after(3000, flip_a_card)

def flip_a_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_image, image=BackImage)

def known_word():
    global learned_count
    if current_card in Words_Data:
        Words_Data.remove(current_card)
        learned_count += 1

    if len(Words_Data) == 0:
        canvas.itemconfig(card_title, text="Finished!", fill="black")
        canvas.itemconfig(card_word, text="You learned all words 🎉", fill="black")
        canvas.itemconfig(card_image, image=FrontImage)
        return
    
    flash_card()


def on_closing():
    result = messagebox.askyesno(
        title="Save Progress",
        message=f"You learned {learned_count} words.\nDo you want to save your progress?")
    
    if result:
        data = pandas.DataFrame(Words_Data)
        data.to_csv("words_to_learn.csv", index=False)
    window.destroy()

# UI Setup
window = Tk()
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)
window.title("Flashy Cards")
window.protocol("WM_DELETE_WINDOW", on_closing)

BackImage = PhotoImage(file=Card_Back)
FrontImage = PhotoImage(file=Card_Front)
WrongImage = PhotoImage(file=Wrong)
CheckImage = PhotoImage(file=Check)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

card_image = canvas.create_image(400, 263, image=FrontImage)
card_title = canvas.create_text(400, 126, text="Title", font=("Arial", 40, "bold"))
card_word = canvas.create_text(400, 326, text="word", font=("Arial", 60, "bold"))

wrong_button = Button(image=WrongImage, bg=BACKGROUND_COLOR,highlightthickness=0, command=flash_card)
wrong_button.grid(row=1, column=0)

check_button = Button(image=CheckImage, bg=BACKGROUND_COLOR,highlightthickness=0, command=known_word)
check_button.grid(row=1, column=1)

flash_card()

window.mainloop()
