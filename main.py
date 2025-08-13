from stats import count_words
from stats import count_characters
from stats import sort_char_dict
import sys
def main():

    
    #num=count_characters("books/frankenstein.txt")
    #'print(count_words("books/frankenstein.txt"))
    #print (num)
    #print(sort_char_dict("books/frankenstein.txt"))
   

    if len(sys.argv)!=2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    path_to_book=(sys.argv[1])
    word_count=count_words(path_to_book)
    char_list=sort_char_dict(path_to_book)


    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_book}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for char_num in char_list:
        print(f"{char_num["char"]}: {char_num["num"]}")
    print("============= END ===============")
  


main()

