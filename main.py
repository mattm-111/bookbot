from stats import get_book_text, word_count, char_count
   


def main():
    word_total = word_count("books/frankenstein.txt")
    print(f"{word_total} words found in the document")
    print(char_count("books/frankenstein.txt"))  

main()