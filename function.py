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

def longest_word(text:str):
    words = find_word(text)
    return(max(words , key=len))
def shortest_word(text:str):
    words= find_word(text)
    return(min(words, key=len))
def more_letter(text:str):
    dic_letter = count_lettler(text)
    return max(dic_letter , key=dic_letter.get)
def min_letter(text:str):
    dic_letter = count_lettler(text)
    return min(dic_letter , key=dic_letter.get)
def max_word(text:str):
    dic_word = count_word(text)
    return max(dic_word , key=dic_word.get)
def min_word(text:str):
    dic_word= count_word(text)
    return min(dic_word , key=dic_word.get)