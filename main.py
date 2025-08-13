from stats import count_words
from stats import count_characters
from stats import sort_char_dict
def main():
    #num=count_characters("books/frankenstein.txt")
    #'print(count_words("books/frankenstein.txt"))
    #print (num)
    #print(sort_char_dict("books/frankenstein.txt"))
    word_count=count_words("books/frankenstein.txt")
    char_list=sort_char_dict("books/frankenstein.txt")

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for char_num in char_list:
        print(f"{char_num["char"]}: {char_num["num"]}")
    print("============= END ===============")
  


main()

