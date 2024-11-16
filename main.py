def main():
    book_path = "/Users/blakedimas/workspace/github.com/blaekd/bookbot/books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = count_words(text)
    char_dict = count_char(text)
    sorted_char_dict = report(char_dict)
    print(text)
    print()
    print("-----BEGIN REPORT OF", book_path, "-----\n")
    print(f"{num_words} words found in the document.\n")
    for char, count in sorted_char_dict.items():
        if char.isalpha():
            print(f"The {char} character was found {count} times.")
    print("\n-----END REPORT-----")


def count_words(text):
    words = text.split()
    return len(words)


def count_char(text):
    text_lower = text.lower()
    characters = list(text_lower)
    char_dict = dict()
    for char in characters:
        char_dict[char] = char_dict.get(char, 0) + 1
    return char_dict

def report(char_dict):
    sorted_char_dict = dict(sorted(char_dict.items(), key=lambda item: item[1], reverse=True))
    return sorted_char_dict

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()