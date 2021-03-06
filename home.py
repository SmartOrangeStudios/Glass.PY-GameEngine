from tkinter import Image, Label
import modulelist as ml

def openwindow():
    root = ml.Tk()
    root.title("Home - Glass.PY")
    root.geometry("700x700")
    root.iconphoto(True, ml.pi(file="Glass.PyLogo.png"))

    windowcontent()

    root.mainloop()

def windowcontent():
    openwindow()
    introTxt = 