# used libraries
from tkinter import *
import pandas
import random

# card design
BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE_FONT = ("Arial", 40, "italic")
WORD_FONT = ("Arial", 60, "bold")

current_card = {}  # empty dictionary for a pair of words that are on the card (English + French)
to_learn = {}  # empty dictionary for words to learn

# see if txt file words_to_learn already exists
try:
    data = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("./data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")  # if doesn't exist --> start from beginning
else:
    to_learn = data.to_dict(orient="records")  # if exists --> continue learning


def next_card():
    """Shows next card"""

    global current_card, flip_timer, to_learn

    window.after_cancel(flip_timer)  # time before another card is shown

    current_card = random.choice(to_learn)  # select random pair of words from words in to_learn

    # show design of the French card
    flash_card.itemconfig(card_img, image=card_front_img)
    flash_card.itemconfig(card_title, text="French", fill="black")
    flash_card.itemconfig(card_word, text=current_card["French"], fill="black")

    flip_timer = window.after(3000, func=flip_card)  # wait before flipping


def is_known():
    """Removes learned card from dict with words to learn and calls next_card()"""

    to_learn.remove(current_card)
    df = pandas.DataFrame(to_learn)
    df.to_csv("./data/words_to_learn.csv", index=False)
    next_card()


def flip_card():
    """Flips card between languages"""

    # show design of the English card
    flash_card.itemconfig(card_img, image=card_back_img)
    flash_card.itemconfig(card_title, text="English", fill="white")
    flash_card.itemconfig(card_word, text=current_card["English"], fill="white")


# set up window for flash cards
window = Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
flip_timer = window.after(3000, func=flip_card)

# load all images
card_back_img = PhotoImage(file="./images/card_back.png")
card_front_img = PhotoImage(file="./images/card_front.png")
check_img = PhotoImage(file="./images/right.png")
cross_img = PhotoImage(file="./images/wrong.png")

# design flash card
flash_card = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
card_img = flash_card.create_image(400, 263, image=card_front_img)
card_title = flash_card.create_text(400, 150, text="", font=LANGUAGE_FONT)
card_word = flash_card.create_text(400, 263, text="", font=WORD_FONT)
flash_card.grid(row=0, column=0, columnspan=2)

# design buttons
unknown_button = Button(image=cross_img, command=next_card, highlightthickness=0, bd=0)
unknown_button.grid(row=1, column=0)
known_button = Button(image=check_img, command=is_known, highlightthickness=0, bd=0)
known_button.grid(row=1, column=1)

next_card()  # get next card

window.mainloop()  # keep window with flash cards open
