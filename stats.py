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

def sort_on(items):
    return items["num"]


def sort_char_dict(book):
    character_dict=count_characters(book)
    list_char_dicts=[]

    for key in character_dict: 
        if key.isalpha():
            char={"char":key,"num":character_dict[key]}
            list_char_dicts.append(char)
    list_char_dicts.sort(reverse=True,key=sort_on)
    return list_char_dicts








   