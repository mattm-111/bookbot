import sys

#takes the txt file and converts to a string
def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()

#gives us the total amount of words in the book    
def word_count(book_path):
    count = len(get_book_text(book_path).split())
    return count

#gives the count of the amount of times each character is used in the book.
#upper and lowercase not counted seperate.

def char_count(book_path):
    book_text = get_book_text(book_path).lower()  #converts all to lower
    char_list = {}
    for c in book_text:
        if c in char_list:
            char_list[c] += 1  #adds count if letter already exists in list
        else:
            char_list[c] = 1   #if letter doesn't exist in the list, add it and set count at 1
    return char_list

#returns a list of just the values in a dict so they can be sorted in another function
def sort_list(list):
    return list["num"]

#sorts our char,  with most used on top
def char_list_pair(book_path):
    new_list = []
    for c, v in char_count(book_path).items():
        if c.isalpha() == True:  #removes all non-alphabet chars
            staged_dict = {}
            staged_dict["char"] = c    #creates a dicts that have "char" char , "num" num key/value pairs
            staged_dict["num"] = v
            new_list.append(staged_dict) #adds the dicts to a  list
        new_list.sort(reverse=True, key=sort_list) #sorts the list by the "num" value, reverse order
    return new_list


#checks to make sure only two args are given
def arg_check(arg_list):
    
    if len(sys.argv) == 2:     
        location_check(sys.argv) #points at a function to make sure we are pointed at a file with writing in it
        return True
    else:
        print("Usage: python3 main.py <path_to_book>") #prints a message and exits if not the correct number of args
        sys.exit(1)

#checks to make sure we can read what is being pointed at in the location arg
def location_check(arg_list): 
    try:
        get_book_text(arg_list[1])
    except Exception as e:    #exits if the file doesn't exist or isn't readable.
        print("Please enter a valid book location")
        sys.exit(1)

   
    


    
   
    





    



