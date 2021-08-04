from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

# read csv using panda
data = pandas.read_csv("./data/french_words.csv")
to_learn = data.to_dict(orient="records")
print(to_learn[0]["French"])


def next_card():
    current_card = random.choice(to_learn)  # eg : {'French': 'vers', 'English': 'towards'}
    # random_english = current_card["English"]
    random_french = current_card["French"]
    canvas.itemconfig(card_title, text="French")  # change the text
    canvas.itemconfig(card_word, text=random_french)  # change the text


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

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
card_title = canvas.create_text(400, 150, font="Ariel 40 italic", text="")
card_word = canvas.create_text(400, 263, font="Ariel 60 bold", text="")

# ---------------------------- Button --------------------------------------#
right_button = Button(image=right_image, highlightthickness=0, command=next_card)
right_button.grid(column=1, row=1)

wrong_button = Button(image=wrong_image, highlightthickness=0, command=next_card)
wrong_button.grid(column=0, row=1)

# show the word on the card after the UI / when start the app
next_card()

window.mainloop()