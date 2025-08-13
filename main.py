def get_book_text(b):
    with open(b) as f:
        book_content=f.read()

    return book_content

from stats import count_words




def main():
    num=count_words("books/frankenstein.txt")
    print (f"{num} words found in the document")




main()
