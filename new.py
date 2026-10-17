from tkinter import *
from tkinter import messagebox 
from pil import Image, ImageTk
window = Tk()
window.title("Image Viewer")
window.geometry("400x420")

title_label = Label(window, text='my photo album',fg='white',bg='purple' , width=40)
title.pack(pady=10)
img_file = Image.open("image2.jpg")
img_file = img_file.resize(( 300, 180))
photo = ImageTk.PhotoImage(img_file)
pic = Label(window, image=photo)
pic.pack(pady=5)

def show_message():
    messagebox.showinfo("Information", "This is my photo album.")
    msg_btn = Button(window, text="Show Info", bg='blue', fg='white', command=show_message)
msg_btn.pack(pady=5)

def show_deatials():
    top = Toplevel()
    top.title("Details")
    top.geometry("200x120")
    info = Label(top, text='location: garden')
    place.pack()
    top.mainloop()
deatials_btn = Button(window, text="Show Details", bg='green', fg='white', command=show_deatials)
deaials_btn.pack(pady=5)

window.mainloop()
