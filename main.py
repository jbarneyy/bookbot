from stats import book_wc, char_count


# Main fuction logic.
def main():

    frankenstein_string = get_book_text("books/frankenstein.txt")
    # print(frankenstein_string)

    num_words = book_wc(frankenstein_string)
    print(f"{num_words} words found in the document")

    unique_char_counts = char_count(frankenstein_string)
    print(f"{unique_char_counts}")


# Function for getting text from file and returning as String.
def get_book_text(filepath):

    book_text = ""
    with open(filepath) as f:
        book_text = f.read()


    return book_text


# Program entry point.
main()