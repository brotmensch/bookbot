from stats import count_words
from stats import count_characters

def main():
    num=count_characters("books/frankenstein.txt")
    print(count_words("books/frankenstein.txt"))
    print (num)




main()
