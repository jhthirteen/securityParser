import sys
import re
import zlib

def read_PDF_binary(file_path):
    file = open(file_path, 'rb')
    binary = file.read()
    if( binary.startswith(b'%PDF-') ): #byte literal %PDF- ensuring that the file's binary is a valid PDF
        return binary
    else:
        return False

def decode_binary(file_to_read):
    file_binary = read_PDF_binary(file_to_read)
    if( file_binary == False ):
        print("Error: " + file_to_read + " is not a PDF")
        exit()
    file_binary_decoded = file_binary.decode('latin1') #standard binary encoding
    return file_binary_decoded

def search_objects(binary_decoded):
    """
    Format for objects: 
    n m obj 
    ... (object content) ...
    endobj
    where n is the object identifier number and m is the generation number
    This can be captured with a regular expression 
    """
    objects = re.findall("\d+ \d+ obj(.*?)endobj", binary_decoded, re.DOTALL)
    return objects

def get_text_streams(objects):
    streams = []
    for obj in objects:
        if( ("stream" in obj) and ("endstream" in obj) ):
            print(obj)

    print(len(objects))



def main():
    file_to_read = sys.argv[1]
    binary_decoded = decode_binary(file_to_read)
    objs = search_objects(binary_decoded)
    get_text_streams(objs)
    

main()