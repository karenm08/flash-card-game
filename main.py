from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# read csv using panda
data = pandas.read_csv("./data/french_words.csv")
french_words_list = data["French"].to_list()
english_words_list = data["English"].to_list()

# pick random a word
random_num = random.randint(0, len(french_words_list)-1)
random_english = english_words_list[random_num]
random_french = french_words_list[random_num]

# same size as the card image
canvas = Canvas(width=800, height=526)
card_front_image = PhotoImage(file="./images/card_front.png")
card_back_image = PhotoImage(file="./images/card_back.png")
right_image = PhotoImage(file="./images/right.png")
wrong_image = PhotoImage(file="./images/wrong.png")

# ---------------------------- Card --------------------------------------#
# half of the width and height to center the card
canvas.create_image(400, 263, image=card_front_image)
canvas.grid(column=0, row=0, columnspan=2)

# cover the white line at the back
canvas.config(bg=BACKGROUND_COLOR,  highlightthickness=0)

# ---------------------------- Text on canvas --------------------------------------#
canvas.create_text(400, 150, font="Ariel 40 italic", text="French")
canvas.create_text(400, 263, font="Ariel 60 bold", text=random_french)

# ---------------------------- Button --------------------------------------#
right_button = Button(image=right_image, highlightthickness=0)
right_button.grid(column=1, row=1)

wrong_button = Button(image=wrong_image, highlightthickness=0)
wrong_button.grid(column=0, row=1)



window.mainloop()