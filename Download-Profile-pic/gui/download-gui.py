from tkinter import *
from tkinter import ttk
import tkinter
import instaloader

def main():
    root = Tk()
    root.geometry('450x450')
    Label(root,text='Username').pack()
    username = Entry(root)
    username.pack()
    Label(root,text='').pack()
    def download():
        instaloader1=instaloader.Instaloader()
        instaloader1.download_profile(username.get(),profile_pic_only=True)
    Button(root,text='Download',command=download).pack()
    root.mainloop()

main()


# made by tt#0009