#imports functions
import sys
from stats import get_book_text, word_count, char_count, char_list_pair, sort_list, arg_check, location_check

   

def main():
    #checks to make sure we get a valid arg with the main command.
    if arg_check(sys.argv) == True:
        print(arg_check)
        book_path = sys.argv[1]
        print("============ BOOKBOT ============")
        print(f'Analyzing book found at {book_path}...')
        print("----------- Word Count ----------")
        print(f'Found {word_count(book_path)} total words')
        print("--------- Character Count -------")
        for chair_pairs in char_list_pair(book_path):
          print(f'{chair_pairs["char"]}: {chair_pairs["num"]}')
        print("============= END ===============")
    else:
        sys.exit
    

 
main()