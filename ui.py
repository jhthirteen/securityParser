import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import os

def buildWindow():

#https://stackoverflow.com/questions/35662844/how-do-i-get-the-entrys-value-in-tkinter
    def get_input(entry):
        print(entry.widget.get())

    window = tk.Tk()
    window.title("File Parser for Security Policies")
    window.geometry("500x500")

    entry = tk.Entry(window, width=40)
    entry.pack()
    entry.bind("<Return>", get_input)

    window.mainloop()


buildWindow()