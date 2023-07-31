import pyshorteners
from tkinter import *


def shortenLink():

    short = pyshorteners.Shortener()
    link = receiverUrl.get()
    link = short.tinyurl.short(link)
    linkLabel = Label(window, text="New Link: ", justify=LEFT, bg='#F0F8FF', font=("Arial", 20))
    linkLabel.place(x=50, y=300)
    newLink = Entry(window, width=25, font=("Arial", 20), fg='blue', bg='#F0F8FF', borderwidth=0)
    newLink.place(x=200, y=300)
    newLink.insert(END, link)



window = Tk()
window.title('URL Shortener')
window.geometry('750x400')
window.config(bg='#F0F8FF')

urlMsg = Label(window, text="URL:", justify=LEFT, bg='#F0F8FF', font=("Arial", 16))
urlMsg.place(x=15, y=40)

receiverUrl = Entry(window, width=45, font=("Arial", 16), borderwidth=0)
receiverUrl.place(x=140, y=40)

shorten = Button(window, text="Shorten it", width=8, height=1, font=("Arial", 20), borderwidth=0, bg="#00BFFF", fg="white", command=shortenLink)
shorten.place(x=280, y=180)



window.mainloop()