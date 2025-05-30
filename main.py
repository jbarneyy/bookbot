import sys
from stats import book_wc, char_count, sorted_char_count


# Main fuction logic.
def main():

    if (len(sys.argv) < 2):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_fp = sys.argv[1]
    book_string = get_book_text(book_fp)
    # print(frankenstein_string)

    num_words = book_wc(book_string)
    # print(f"Found {num_words} total words")

    unique_char_counts = char_count(book_string)
    # print(f"{unique_char_counts}")

    sorted_list_of_chars = sorted_char_count(unique_char_counts)
    # print(f"{sorted_list_of_chars}")

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_fp}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for i in sorted_list_of_chars:
        print(f"{i["char"]}: {i["num"]}")

    print("============= END ===============")

# Function for getting text from file and returning as String.
def get_book_text(filepath):

    book_text = ""
    with open(filepath) as f:
        book_text = f.read()


    return book_text


# Program entry point.
main()