# # check this code first.
# from tkinter import *

# app = Tk()
# # The title of the project
# app.title("The title of the project")
# # The size of the window
# app.geometry("400x400")


# def c():
#     # Label
#     m = Label(app, text="Text")
#     m.pack()


# # Button
# l = Button(app, text="The text of the Butoon", command=c)
# # Packing the Button
# l.pack()
# app.mainloop()
from procesarImg import *
from screenShot import *
from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image

fuente="-weight bold"
window = tk.Tk()
path="C:/EjerciciosHackademy/chat.png"


img = ImageTk.PhotoImage(Image.open(path))


frame1 = tk.Frame(master=window, width=200, height=100, bg="red")
frame1.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

panel = tk.Label(master=frame1, image = img).pack()


frame2 = tk.Frame(master=window, width=100, bg="#808B96" )
frame2.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

frame3 = tk.Frame(master=window, width=50,bg="#808B96" )
frame3.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

bt1=Button(master=frame2, text="Screenshot",font=fuente,relief="flat", borderwidth=5,width=10, height=2,background="#AED6F1",command=fScreenshot)
bt1.pack(fill=tk.BOTH,  expand=True)

bt2=Button(master=frame2, text=" Procesar ",font=fuente,relief="flat", borderwidth=5,width=10, height=2,background="#85C1E9",command=fProesamiento)
bt2.pack(fill=tk.BOTH,  expand=True)

bt3=Button(master=frame2, text=" Analizar ",font=fuente,relief="flat", borderwidth=5,width=10, height=2,background="#5DADE2",command=fAnalizar)
bt3.pack(fill=tk.BOTH,  expand=True)






window.mainloop()

