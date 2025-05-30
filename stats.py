
# Accepts text from book as a String, returns the number of words in the String.
def book_wc(book_as_string):

    return len(book_as_string.split())


# Takes the text from the book as a string, and returns the number of times each character, (including symbols and spaces), appears in the string.
def char_count(book_as_string):
    book_as_string = book_as_string.lower()
    characters = {}

    for c in book_as_string:

        if c in characters:
            characters[c] += 1
        else:
            characters[c] = 1

    return characters


# Takes the dictionary of characters and returns a sorted list of dictionaries. Also filters so only alphabetical characters are included.
def sorted_char_count(char_dict):

    dict_list = []

    for k in char_dict:

        if not k.isalpha():
            continue

        single_dict_item = {"char": k, "num": char_dict[k]}
        
        dict_list.append(single_dict_item)


    dict_list.sort(key = lambda x: x["num"], reverse = True)
    return dict_list
