def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()
    
def word_count(book_path):
    count = len(get_book_text(book_path).split())
    return count
   
#commeted out for assignment
#def main():
 #   print(get_book_text("books/frankenstein.txt"))

def main():
    word_total = word_count("books/frankenstein.txt")
    print(f"{word_total} words found in the document")  

main()