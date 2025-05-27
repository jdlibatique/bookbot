def get_number_of_words(book_text):
    return book_text.split()


def count_individual_letters(book_text):
    letters = {}

    for char in book_text:
        lowered_char = char.lower()
        if lowered_char in letters:
            letters[lowered_char] += 1
        else:
            letters[lowered_char] = 1
    return letters


def sort_on(key):
    return key["num"]


def sort_letter_count(letter_count):
    sorted_dicts = []

    for entry in letter_count:
        if entry.isalpha():
            sorted_dicts.append({"char": entry, "num": letter_count[entry]})

    sorted_dicts.sort(key=sort_on, reverse=True)
    return sorted_dicts
