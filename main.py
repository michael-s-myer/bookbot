from stats import count_words
from stats import character_count
from stats import sort_dict
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()

    return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_name = sys.argv[1]

    book_text = get_book_text(book_name)

    book_length = count_words(book_text)

    total_char = character_count(book_text)
    
    sorted_total = sort_dict(total_char)

    print("============ BOOKBOT ============")

    print(f"Analyzing book found at {book_name}...")

    print("----------- Word Count ----------")

    print(f"Found {book_length} total words")

    print("--------- Character Count -------")

    for char_dict in sorted_total:
        char = char_dict["char"]
        count = char_dict["count"]
        if char.isalpha():
            print(f"{char}: {count}")

    print("============= END ===============")

main()
