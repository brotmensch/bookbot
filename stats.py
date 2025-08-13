def count_words(t):
    text=get_book_text(t)
    words=text.split()
    return len(words)

def get_book_text(b):
    with open(b) as f:
        book_content=f.read()

    return book_content