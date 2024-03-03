def main():
    while True:
        file_path = input("Enter the path to your document: (↵ for 'books/frankenstein.txt') ")

        if not file_path:
            file_path = "books/frankenstein.txt"

        book_text = get_book_text(file_path)

        if book_text is not None:
            word_count = get_word_count(book_text)
            letters_dict = get_letters_dict(book_text)

            print(f"--- Begin report of {file_path} ---")
            print(f"{word_count} words found in the document")
            aggregate_letters(letters_dict)
            print("--- End report ---")
            break
        else:
            print("Try again...")
            continue


def get_book_text(file_path):
    try:
        with open(file_path, "r") as file:
            return file.read()
    except FileNotFoundError:
        print("File not found")
        return None
    except PermissionError:
        print("No permission to read this file")
        return None
    except Exception as e:
        print(e)
        return None


def get_word_count(text):
    return len(text.split())


def get_letters_dict(text):
    letters = {}

    for ch in text:
        if not ch.isalpha():
            continue

        ch = ch.lower()
        if ch in letters:
            letters[ch] += 1
        else:
            letters[ch] = 1

    return letters


def aggregate_letters(letters):
    letters_list = []

    for letter in letters:
        dict = {"char": letter, "count": letters[letter]}
        letters_list.append(dict)

    letters_list.sort(reverse=True, key=(lambda dict : dict["count"]))
    
    for letter in letters_list:
        print(f"The '{letter["char"]}' character was found {letter["count"]} times")


main()