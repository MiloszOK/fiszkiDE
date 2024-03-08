import tkinter as tk

window = tk.Tk()
window.title('Fiszki (prawie ryby)')
window.config(padx=50, pady=50, bg='#b1ddc6')

# ------------------ GUI ----------------- #

fiszkaPhotoB = tk.PhotoImage(file='card_front.png')
fiszkaCanB = tk.Canvas(width=800, height=526, bg='#b1ddc6', highlightthickness=0)
fiszkaCanB.create_image(400,263,image=fiszkaPhotoB)
fiszkaCanB.create_text(400,150,text='Niemiecki', font=('Ariel',40,'italic'))
fiszkaCanB.create_text(400, 280, text='123', font=('Ariel', 60, 'bold'))
fiszkaCanB.grid(column=0, row=0, columnspan=2)


fiszkaPhotoC = tk.PhotoImage(file='card_back.png')


obrazX = tk.PhotoImage(file='x.png')
x = tk.Button(image=obrazX, bg='#b1ddc6', borderwidth=0, activebackground='#799787')
x.grid(column=0, row=1)

obrazT = tk.PhotoImage(file='t.png')
t = tk.Button(image=obrazT, width=50, height=50, bg='#b1ddc6', borderwidth=0, activebackground='#799787')
t.grid(column=1, row=1)





window.mainloop()