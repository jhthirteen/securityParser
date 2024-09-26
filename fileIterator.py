import zipfile
import shutil
import os
import xml.etree.ElementTree as ElementTree

def unzip_docx(file_path):
    docx = zipfile.ZipFile(file_path, 'r')
    docx.extract('word/document.xml') #extract the xml file containing text contents 
    shutil.move('./word/document.xml', '.') #move to home directory
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

def search_for_text(input_str, files):
    pass

unzip_docx('ir.docx')
print(get_text(get_xml_root('document.xml')))