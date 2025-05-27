from stats import get_number_of_words, count_individual_letters, \
    sort_letter_count
import sys


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    number_of_words = len(get_number_of_words(book_text))
    letter_count = count_individual_letters(book_text)
    sorted_letter_count = sort_letter_count(letter_count)

    print_report(book_path, number_of_words, sorted_letter_count)


def get_book_text(filepath):
    with open(filepath) as file:
        return file.read()


def print_report(book_path, number_of_words, sorted_letter_count):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {number_of_words} total words")
    print("--------- Character Count -------")

    for entry in sorted_letter_count:
        print(f"{entry['char']}: {entry['num']}")

    print("============= END ===============")


main()
