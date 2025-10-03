# https://kanye.rest/
from tkinter import *
import requests


def get_quote():
    response = requests.get("https://api.kanye.rest")
    response.raise_for_status()
    data = response.json()
    quote = data["quote"]
    canvas.itemconfig(quote_text, text=quote)
    
    # Start with a big font size and shrink if needed
    font_size = 30
    while True:
        canvas.itemconfig(
            quote_text,
            text=quote,
            font=("Arial", font_size, "bold")
        )
        bbox = canvas.bbox(quote_text)  # (x1, y1, x2, y2) of the text
        if bbox and (bbox[2] - bbox[0] <= 250 and bbox[3] - bbox[1] <= 300):
            break
        font_size -= 2
        if font_size < 10:  # avoid infinite loop
            break

window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250, font=("Arial", 30, "bold"), fill="white")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)



window.mainloop()