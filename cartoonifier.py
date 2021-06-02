import tkinter as tk
from tkinter import *
from cartoonizer import *
from tkinter import filedialog
from PIL import ImageTk, Image
import cv2

top = tk.Tk()
top.geometry('1000x600')
top.title('Cartoonifier')
top.iconbitmap("D:\so_cket\Courses\cartoonifier\Lib\pics\p.png")
top.config(background="white")


def save_cartoon(file_path, cartoon_img):
    where = filedialog.asksaveasfilename(filetypes=(('JPEG Files', '*.jpg'), ('PNG Files', '*.png'),
                                                    ("All Files", "*.*")), defaultextension=file_path[-4:])
    cartoon_img.save(where)


def show_save_button(file_path, cartoon_img):
    save_b = Button(top, text="Save Cartoon", command=lambda: save_cartoon(file_path, cartoon_img), padx=10, pady=5)
    save_b.place(relx=0.69, rely=0.86)


def convert(file_path):
    cartoon = make_cartoon(file_path)
    cartoon = cv2.cvtColor(cartoon, cv2.COLOR_BGR2RGB)
    cartoon_img = Image.fromarray(cartoon)
    cartoon_img.thumbnail(((top.winfo_width() / 1.8), (top.winfo_height() / 1.8)))
    im = ImageTk.PhotoImage(cartoon_img)
    label = Label(top, image=im)
    label.image = im
    label.pack(side="right", expand='yes')
    show_save_button(file_path, cartoon_img)


def show_convert_button(file_path):
    convert_b = Button(top, text="Cartoonify", command=lambda: convert(file_path), padx=10, pady=5)
    convert_b.place(relx=0.79, rely=0.46)


def upload_image():
    file_path = filedialog.askopenfilename()
    uploaded = Image.open(file_path)
    uploaded.thumbnail(((top.winfo_width() / 2.25), (top.winfo_height() / 2.25)))
    im = ImageTk.PhotoImage(uploaded)
    label = Label(top, image=im)
    label.image = im
    label.pack(side="left", expand='yes')
    show_convert_button(file_path)


upload = Button(top, text="Upload an Image", command=upload_image, pady=5)
upload.config(background="#adadee", foreground="white", font=("arial", 10, "bold"))
upload.place(relx=0.44, rely=0.86)

top.mainloop()
