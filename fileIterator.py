import zipfile
import shutil
import os
import sys
import xml.etree.ElementTree as ElementTree

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
        print(text)
        
def main():
    if( len(sys.argv) < 2 ):
        print("invoke as python3 fileIterator.py <file1> <file2> ... <file n>")
        exit()

    input_files = [None] * (len(sys.argv) - 1) #initialize array for sizse of files 

    for i in range(1, len(sys.argv)): #takes files as command line args
        input_files[i-1] = sys.argv[i]

    initParser()
    pull_xml(input_files)
    search_for_text("monitoring", input_files)

main()