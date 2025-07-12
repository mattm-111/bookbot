import sys
from stats import get_book_text, word_count, char_count, char_list_pair, sort_list

   


def arg_check():
    
    if len(sys.argv) == 2:
        location_check()
        main()
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

def location_check():
    try:
        get_book_text(sys.argv[1])
    except Exception as e:
        print("Please enter a valid book location")
        sys.exit(1)
    

def main():
    book_path = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f'Analyzing book found at {book_path}...')
    print("----------- Word Count ----------")
    print(f'Found {word_count(book_path)} total words')
    print("--------- Character Count -------")
    for chair_pairs in char_list_pair(book_path):
        print(f'{chair_pairs["char"]}: {chair_pairs["num"]}')
    print("============= END ===============")

    

 
arg_check()