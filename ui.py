import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import os

input = ""

def buildWindow():


    def get_input():
        input = entry.get()

    window = tk.Tk()
    window.title("File Parser for Security Policies")
    window.geometry("500x500")

    entry = tk.Entry(window, width=40)
    entry.pack()
    
    submit = tk.Button(window, text="Enter", command=get_input())
    submit.pack()

    window.mainloop()

    print(input)



buildWindow()