def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()
    
def word_count(book_path):
    count = len(get_book_text(book_path).split())
    return count