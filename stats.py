def count_words(t):
    text=get_book_text(t)
    words=text.split()
    return len(words)

def get_book_text(b):
    with open(b) as f:
        book_content=f.read()

    return book_content

def count_characters(c):
    c=get_book_text(c)
    low_text=c.lower()
    character_count={}
    for character in low_text:
        if character in character_count:
            character_count[character]+=1
        else:
            character_count[character]=1
    






    return character_count
