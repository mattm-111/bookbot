def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()
    
def word_count(book_path):
    count = len(get_book_text(book_path).split())
    return count

def char_count(book_path):
    book_text = get_book_text(book_path).lower()
    char_list = {}
    for c in book_text:
        if c in char_list:
            char_list[c] += 1
        else:
            char_list[c] = 1
    return char_list

def sort_list(list):
    return list["num"]


def char_list_pair(book_path):
    new_list = []
    for c, v in char_count(book_path).items():
        if c.isalpha() == True:
            staged_dict = {}
            staged_dict["char"] = c
            staged_dict["num"] = v
            new_list.append(staged_dict)
        new_list.sort(reverse=True, key=sort_list)
    return new_list


   
    


    
   
    





    



