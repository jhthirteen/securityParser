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
    window.geometry("1000x1000")

    entry = tk.Entry(window, width=40)
    entry.pack()
    entry.bind("<Return>", get_input)

    intro = tk.StringVar(window, "Quick .docx parser")
    intro_label = tk.Label(window, textvariable=intro)
    intro_label.pack()

    step_one = tk.StringVar(window, "1) Enter a keyword you wish to search for and press the ENTER key")
    step_one_label = tk.Label(window, textvariable=step_one)
    step_one_label.pack()

    step_two = tk.StringVar(window, "2) A file dialog window will appear, select the files you wish to search. To select multiple files, click and drag the highlight box")
    step_two_label = tk.Label(window, textvariable=step_two)
    step_two_label.pack()

    step_three = tk.StringVar(window, "3) Results of a search for each individual file will be outputted to the terminal")
    step_three_label = tk.Label(window, textvariable=step_three)
    step_three_label.pack()

    window.mainloop()


buildWindow()