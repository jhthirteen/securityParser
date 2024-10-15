import zipfile
import shutil
import os
import sys
import xml.etree.ElementTree as ElementTree
import tkinter as tk
from tkinter import filedialog

debug = False

def build_window():
    keyword = []
    def get_input(entry): #function that adds whatever string is entered in the field to the keyword array
        keyword.append(entry.widget.get()) #append the word the user entered in a box 
        window.destroy()
    
    window = tk.Tk()
    window.title("File Parser for Security Policies")
    window.geometry("1000x1000")

    entry = tk.Entry(window, width=40)
    entry.pack() #adds entry filed to the window 
    entry.bind("<Return>", get_input) #key-binds the return key to call get_input function 

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

    window.mainloop() #infinite loop that runs until key return key is entered 
    
    return keyword[0]

def clean():
    try:
        shutil.rmtree('text_docs')
    except:
        print("no 'text_docs directory found to delete")

def unzip_docx(file_path):
    docx = zipfile.ZipFile(file_path, 'r')
    docx.extract('word/document.xml') #extract the xml file containing text contents
    end_location = file_path.find('.')
    file_name = './text_docs/' + file_path[0:end_location] + '.xml'
    shutil.move('./word/document.xml', './text_docs') #move to home directory
    os.rename('./text_docs/document.xml', file_name)
    os.rmdir('./word') #delete the extracted directory

def get_xml_root(file_path): #(./extracted_info/word/document.xml) path 
    xml_tree = ElementTree.parse(file_path) #creates an parse tree out out of the xml file passed in 
    xml_tree_root = xml_tree.getroot() #returns the root of this parse tree
    return xml_tree_root

def get_text(xml_tree_root):
    nsmap = {'w' : 'http://schemas.openxmlformats.org/wordprocessingml/2006/main' }
    all_xml_text = xml_tree_root.findall('.//w:t', nsmap)
    text_formatted = [None] * len(all_xml_text) #initialize a second array to hold .text part of these objects
    for i in range(len(all_xml_text)):
        text_formatted[i] = all_xml_text[i].text

    return(text_formatted)

def initParser():
    os.mkdir('text_docs')

def pull_xml(files):
    for i in range(len(files)): #pull all xml files out
        unzip_docx(files[i])

def search_for_text(key, files):
    for i in range(len(files)):
        end_location = files[i].find('.')
        file_name = './text_docs/' + files[i][0:end_location] + '.xml'
        root = get_xml_root(file_name)
        text = get_text(root)
        instances = 0
        print("\nSearching " + files[i][0:end_location] + '.xml' + ' for ' + key + ':\n')
        for i in range(len(text)):
            if( text[i].find(key) > 0 ):
                instances += 1
                print("Found instance " + str(instances) + ":\n" + text[i])
        
        if( instances == 0 ):
            print("No instances found")
        
def main():

    if( not debug ): #code we want to execute 

        keyword = build_window()

        if( keyword == "" ): #error handling to ensure some string was entered 
            print("ERROR: Please enter a valid keyword to search files for")
            exit()

        files = filedialog.askopenfilenames()
        file_names = [None] * len(files)
        for i in range(len(files)):
            start_location = files[i].rfind('/')
            file_names[i] = files[i][start_location+1:len(files[i])]

        #window.mainloop()

        initParser()
        pull_xml(file_names)
        search_for_text(keyword, file_names)
        clean()

    if( debug ): #code to test if we want to debug 
        print(len(sys.argv))

main()