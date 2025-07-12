from stats import get_book_text, word_count
   
#commeted out for assignment
#def main():
 #   print(get_book_text("books/frankenstein.txt"))

def main():
    word_total = word_count("books/frankenstein.txt")
    print(f"{word_total} words found in the document")  

main()