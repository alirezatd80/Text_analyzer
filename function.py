import re

def find_word(string):
    words = re.findall(r'\w+' , string)
    return words

def find_sentences(string:str):
    sentences = re.split(r'(?<=[\.\?!])\s*|\n\s*' , string.strip())
    return sentences

def count_word(string):
    words = find_word(string)
    return {word: words.count(word) for word in words}
