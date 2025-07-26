
def get_num_words(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    number_of_words = len(file_contents.split())

    return f"Found {number_of_words} total words"


def count_letters(filepath):

    with open(filepath) as f:
        file_contents = f.read()

    file = file_contents.lower() #lower the letters to avoid duplication
    count_letters = {} #initiated the epty dictionay
    
    
    for words in file:

        if words.isalpha():
            if words in count_letters:
                count_letters[words] += 1
            else:
                count_letters[words] = 1    
    return count_letters


#if __name__ == '__main__':
    print(get_num_words(r'/home/omer_khan/bootdev_projects/bookbot/books/frankenstein.txt'))
