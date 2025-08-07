from function import find_word,find_sentences,count_word,count_lettler,longest_word,shortest_word,more_letter,min_letter,max_word,min_word


def main ():
    print('welcome to this ')
    while True:
        order = int(input('1 for analize text \n2 for exit\n'))
        if order == 1 :
            text = input('enter your text : ')
            number_word = len(find_word(text))
            number_sentences = len(find_sentences(text))
            moreword = max_word(text)
            lessword = min_word(text)
            moreletter = more_letter(text)
            minletter = min_letter(text)
            long_word = longest_word(text)
            short_word = shortest_word(text)
            print(f"""
                  result = 
                  number of sentence = {number_sentences-1}
                  number of word = {number_word}
                  the most frequent word = {moreword}
                  The least frequent word = {lessword}
                  the most frequent letter = {moreletter}
                  the least frequent letter = {minletter}
                  The longest word = {long_word}
                  The shortest word = {short_word}
                  """)
        if order == 2 :
            break
        
        
        
        
        
if __name__ == "__main__":
    main()