from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50)
window.config(bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526)
card_front = PhotoImage(file="./images/card_front.png")
card_back = PhotoImage(file="./images/card_back.png")
right = PhotoImage(file="./images/right.png")
wrong = PhotoImage(file="./images/wrong.png")

# Card
canvas.create_image(400, 270, image=card_front)
canvas.grid(column=0, row=0,columnspan=2)

# Text on canvas
canvas.create_text(400, 150, font="Ariel 40 italic", text="French")
canvas.create_text(400, 263, font="Ariel 60 bold", text="Trouve")

# Button
right_button = Button(image=right, highlightthickness=0)
right_button.grid(column=1, row=1)

wrong_button = Button(image=wrong, highlightthickness=0)
wrong_button.grid(column=0, row=1)



window.mainloop()