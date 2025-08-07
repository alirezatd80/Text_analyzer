import re
import string

def find_word(text:str):
    words = re.findall(r'\w+' , text)
    return words

def find_sentences(text:str):
    sentences = re.split(r'(?<=[\.\?!])\s*|\n\s*' , text.strip())
    return sentences

def count_word(text:str):
    words = find_word(text)
    return {word: words.count(word) for word in words}

def count_lettler(text:str):
    letters = list(string.ascii_lowercase)
    return {letter: text.count(letter) for letter in letters}