from tkinter import *
import requests
import random

url = "https://waifu.it/api/v4/quote"
ACCESS_TOKEN = "NzQwMjI2MzI0NDgzODAxMTEx.MTcxODE1NTE4NA--.2644097bf7"
BG_COLOUR = "#AFEEEE"

def get_quote():
    quote_fetched = False
    while not quote_fetched:
        response = requests.get(url, headers={"Authorization": ACCESS_TOKEN})
        response.raise_for_status()
        data = response.json()
        if (len(data["quote"]) < 180) & (len(data["anime"]) < 35):
            print(f'{len(data["anime"])} {len(data["quote"])} {data["quote"]}')
            canvas.itemconfig(anime_name_text, text=data["anime"])
            if len(data["quote"]) > 140:
                canvas.itemconfig(quote_text, text=data["quote"], font=("Courier", 22, "italic"))
            elif len(data["quote"]) < 60:
                canvas.itemconfig(quote_text, text=data["quote"], font=("Courier", 28, "italic"))
            else:
                canvas.itemconfig(quote_text, text=data["quote"], font=("Courier", 25, "italic"))
            quote_fetched = True


window = Tk()
window.title("Anime Quote Generator")

canvas = Canvas(width=462, height=648)
quote_bg_img = PhotoImage(file="images/quote_bg_2.png")
quote_bg = canvas.create_image(231, 341, image=quote_bg_img)
anime_name_text = canvas.create_text(231, 250, text="", justify="center", width=375,
                                font=("Courier", 35, "bold"), fill="#BC8F8F")
quote_text = canvas.create_text(231, 380, text="Tap Xiao 🌱", justify="center", width=370,
                                font=("Courier", 30), fill="#BC8F8F")
canvas.grid(row=0, column=0, rowspan=4)

xiao_img = PhotoImage(file="images/xiao_icon_small.png")
xiao_button = Button(image=xiao_img, border=0, highlightthickness=0, command=get_quote)
xiao_button.grid(row=3, column=0)

window.mainloop()
