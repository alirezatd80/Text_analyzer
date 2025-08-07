import re

def find_word(string):
    words = re.findall(r'\w+' , string)
    return words


