import tkinter as tk

import pandas
import pandas as pd
import random

slowo = {}


# ------------------ FUNKCJE -----------------#
def losoweSl():
    global slowo, flip
    window.after_cancel(flip)
    slowo = random.choice(slowaDF)

    fiszkaCanB.itemconfig(kartka, image=fiszkaPhotoB)
    fiszkaCanB.itemconfig(slowka, text=slowo['German'], fill='white')
    fiszkaCanB.itemconfig(jezyk, text='Deutsch', fill='white')
    flip = window.after(3000, func=polSl)

def polSl():
    fiszkaCanB.itemconfig(kartka, image=fiszkaPhotoC)
    fiszkaCanB.itemconfig(slowka, text=slowo['Polski'], fill='black')
    fiszkaCanB.itemconfig(jezyk, text='Polski', fill='black')

def znana():
    slowaDF.remove(slowo)
    data = pandas.DataFrame(slowaDF)
    data.to_csv('csv/slowa_do_nauki.csv', index=False)
    losoweSl()

# ------------------ GUI ----------------- #

window = tk.Tk()
window.title('Fiszki (prawie ryby)')
window.config(padx=50, pady=50, bg='#b1ddc6')

try:
    slowaDF = pd.DataFrame.to_dict(pd.read_csv('csv/slowa_do_nauki.csv'), orient='records')
except FileNotFoundError:
    slowaDF = pd.DataFrame.to_dict(pd.read_csv('csv/slowa_de.csv'), orient='records')


flip = window.after(3000, func=polSl)

fiszkaPhotoB = tk.PhotoImage(file='image/card_back.png')
fiszkaPhotoC = tk.PhotoImage(file='image/card_front.png')
fiszkaCanB = tk.Canvas(width=800, height=526, bg='#b1ddc6', highlightthickness=0)
kartka = fiszkaCanB.create_image(400, 263, image=fiszkaPhotoB)
jezyk = fiszkaCanB.create_text(400, 150, text='Deutsch', font=('Ariel', 40, 'italic'), fill='white')
slowka = fiszkaCanB.create_text(400, 280, text=slowaDF[random.randint(1, len(slowaDF) - 1)]['German'], font=('Ariel', 60, 'bold'), fill='white')
fiszkaCanB.grid(column=0, row=0, columnspan=2)
losoweSl()

obrazX = tk.PhotoImage(file='image/x.png')
x = tk.Button(image=obrazX, bg='#b1ddc6', borderwidth=0, activebackground='#799787', command=losoweSl)
x.grid(column=0, row=1)

obrazT = tk.PhotoImage(file='image/t.png')
t = tk.Button(image=obrazT, width=50, height=50, bg='#b1ddc6', borderwidth=0, activebackground='#799787', command=znana)
t.grid(column=1, row=1)

window.mainloop()
