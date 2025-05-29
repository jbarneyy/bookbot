
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