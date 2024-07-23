# openBook reads and return the whole book in string format
def openBook(path):
        print(path)
        with open(f'{path}') as f:
            file_content = f.read()
            return file_content

# count words in the book
def count_words(string):
     return len(string.split())
     

# counts the number of character
def char_count(string):
    string = string.lower() 
    list_of_char = string.split(' ')
    string = "".join(list_of_char).lower()
    char_dict = {}
    for char in string:
        if char in char_dict:
            char_dict[char] = char_dict.get(char)+1
        else:
             char_dict[char]=1
    
    return char_dict

# display the character dict
def display_char (dict):
    char_list = []
    for key in dict:
        if key.isalpha():
              char_list.append(key)
    char_list.sort()
    for item in char_list:
        print(f"The '{item}' character was found {dict.get(item)} times") 

def main ():
    path = input('Please input the relative path of the book (for ex: /books/*.txt): ')
    string = openBook(path)
    print(f"\n---Begin report of {path}---")

    print(f"\n{count_words(string)} words found in the document \n")    
    display_char(char_count(string))
    print("\n--- End report ---")
    
main()