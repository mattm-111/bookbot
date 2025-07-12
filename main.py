from stats import get_book_text, word_count, char_count, char_list_pair, sort_list
   
book_path = "books/frankenstein.txt"

def main():
    print("============ BOOKBOT ============")
    print(f'Analyzing book found at {book_path}...')
    print("----------- Word Count ----------")
    print(f'Found {word_count(book_path)} total words')
    print("--------- Character Count -------")
    for chair_pairs in char_list_pair(book_path):
        print(f'{chair_pairs["char"]}: {chair_pairs["num"]}')
    print("============= END ===============")

    

 
main()